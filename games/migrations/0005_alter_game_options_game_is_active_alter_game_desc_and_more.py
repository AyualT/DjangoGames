# Generated by Django 4.2 on 2023-04-27 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_trailer_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-release_date', 'title'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='game',
            name='engine',
            field=models.CharField(max_length=100, verbose_name='Игровой Движок'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='game',
            name='poster',
            field=models.ImageField(null=True, upload_to='game_posters', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Цена $'),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating_ign',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Оценка IGN'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating_metacritic',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Оценка Metacritic'),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(verbose_name='Дата Релиза'),
        ),
        migrations.AlterField(
            model_name='game',
            name='studio',
            field=models.CharField(max_length=100, verbose_name='Студия Разработчик'),
        ),
        migrations.AlterField(
            model_name='game',
            name='style',
            field=models.CharField(max_length=200, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='game',
            name='trailer_url',
            field=models.URLField(blank=True, null=True, verbose_name='Трейлер (Ссылка)'),
        ),
    ]