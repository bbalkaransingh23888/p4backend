# Generated by Django 3.1.1 on 2020-09-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p4_api', '0008_game_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_url',
            field=models.URLField(blank=True),
        ),
    ]
