# Generated by Django 2.1.4 on 2018-12-05 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181205_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourites',
        ),
    ]
