# Generated by Django 3.1.1 on 2020-09-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p4_api', '0003_auto_20200915_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]