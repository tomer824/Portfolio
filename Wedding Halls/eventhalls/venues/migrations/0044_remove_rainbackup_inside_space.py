# Generated by Django 3.1 on 2020-09-08 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0043_auto_20200907_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rainbackup',
            name='inside_space',
        ),
    ]
