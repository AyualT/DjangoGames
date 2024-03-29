# Generated by Django 4.2 on 2023-05-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='founded',
            field=models.DateField(verbose_name='Основано'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='founder',
            field=models.CharField(max_length=200, verbose_name='Основатель'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='headquarters',
            field=models.CharField(max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='main_site',
            field=models.URLField(verbose_name='Главная Страница'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
    ]
