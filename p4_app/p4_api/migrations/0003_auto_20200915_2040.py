# Generated by Django 3.1.1 on 2020-09-15 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p4_api', '0002_auto_20200915_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
    ]
