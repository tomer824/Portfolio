# Generated by Django 3.1 on 2020-09-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200907_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
