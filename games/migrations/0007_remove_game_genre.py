# Generated by Django 4.2 on 2023-04-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
    ]
