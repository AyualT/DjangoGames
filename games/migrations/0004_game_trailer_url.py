# Generated by Django 4.2 on 2023-04-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='trailer_url',
            field=models.URLField(null=True),
        ),
    ]
