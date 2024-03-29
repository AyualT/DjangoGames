# Generated by Django 4.2 on 2023-05-01 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
        ('studios', '0002_studio_logo'),
        ('games', '0009_remove_game_publisher_remove_game_studio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='publishers.publisher', verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='studios.studio', verbose_name='Студия Разработчик'),
        ),
    ]
