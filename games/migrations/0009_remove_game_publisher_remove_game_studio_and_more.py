# Generated by Django 4.2 on 2023-05-01 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_game_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='game',
            name='studio',
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.genre', verbose_name='Жанр'),
        ),
    ]
