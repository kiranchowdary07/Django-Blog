# Generated by Django 2.1.3 on 2019-03-26 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20190326_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title2',
        ),
    ]
