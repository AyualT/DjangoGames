# Generated by Django 4.2 on 2023-04-27 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='games.genre', verbose_name='Жанр'),
        ),
    ]
