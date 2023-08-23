from django.db import models

from hitcount.models import HitCount
from hitcount.models import HitCountMixin

from django.contrib.contenttypes.fields import GenericRelation

class Publisher(models.Model, HitCountMixin):
    name = models.CharField(max_length=100,verbose_name='Издатель')
    desc = models.TextField(verbose_name='Описание')
    founder = models.CharField(max_length=200,verbose_name='Основатель')
    founded = models.DateField(verbose_name='Основано')
    headquarters = models.CharField(max_length=200,verbose_name='Адрес')
    main_site = models.URLField(max_length=200,verbose_name='Главная Страница')
    is_active = models.BooleanField(default=True,verbose_name='Активен')

    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def current_hitcount(self):
        return self.hit_count.hits
    
    def current_hitcount_in_last(self, num):
        return self.hit_count.hits_in_last(days=num)

    def __str__(self) -> str:
        return self.name