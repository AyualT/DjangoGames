# Generated by Django 4.2 on 2023-04-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headquarters', models.CharField(max_length=100)),
                ('founder', models.CharField(max_length=200)),
                ('founded', models.DateField()),
                ('games', models.TextField()),
                ('main_site', models.URLField()),
            ],
        ),
    ]
