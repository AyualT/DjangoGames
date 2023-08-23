# Generated by Django 4.2 on 2023-05-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0002_studio_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='founded',
            field=models.DateField(verbose_name='Основано'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='founder',
            field=models.CharField(max_length=200, verbose_name='Основатель'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='games',
            field=models.TextField(verbose_name='Список игр'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='headquarters',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='logo',
            field=models.ImageField(null=True, upload_to='studio_logos', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='main_site',
            field=models.URLField(verbose_name='Главная Страница'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
    ]
