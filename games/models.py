from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from studios.models import Studio
from publishers.models import Publisher

from hitcount.models import HitCount
from hitcount.models import HitCountMixin

from django.contrib.contenttypes.fields import GenericRelation

class Game(models.Model, HitCountMixin):
    title = models.CharField(max_length=200, verbose_name='Название')
    poster = models.ImageField(upload_to='game_posters',null=True, verbose_name='Обложка')
    trailer_url = models.URLField(max_length=200,null=True, blank=True, verbose_name='Трейлер (Ссылка)')
    studio = models.ForeignKey(Studio,on_delete=models.PROTECT,null=True,blank=True, verbose_name='Студия Разработчик')
    genre = models.ForeignKey('Genre',on_delete=models.PROTECT,verbose_name="Жанр")
    style = models.CharField(max_length=200, verbose_name='Стиль')
    desc = models.TextField(verbose_name='Описание')
    release_date = models.DateField(verbose_name='Дата Релиза')
    publisher = models.ForeignKey(Publisher,on_delete=models.PROTECT,null=True,blank=True,verbose_name='Издатель')
    rating_metacritic = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100), 
        ],
        verbose_name='Оценка Metacritic'
    )   
    rating_ign = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ], 
        verbose_name='Оценка IGN'
    )
    engine = models.CharField(max_length=100, verbose_name='Игровой Движок')
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
        ], 
        verbose_name='Цена $'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    
    def current_hitcount(self):
        return self.hit_count.hits
    
    def current_hitcount_in_last(self, num):
        return self.hit_count.hits_in_last(days=num)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('game_detail',args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-release_date','title']

from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    rating_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    rating_choise = (
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    rating = models.IntegerField(choices=rating_choise, default=6, verbose_name='Рейтинг')
    comment = models.TextField(verbose_name='Ревью')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    def __str__(self) -> str:
        return f'{self.game.title} by {self.author}'

class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    value_choise=(
        (0,0),
        (1,1),
    )
    value = models.IntegerField(choices=value_choise)

    def __str__(self) -> str:
        return f'Review: {self.review} | User: {self.user} {self.value}'

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.genre