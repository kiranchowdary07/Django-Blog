# Generated by Django 2.1.3 on 2019-02-21 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20190221_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='published_date',
        ),
    ]