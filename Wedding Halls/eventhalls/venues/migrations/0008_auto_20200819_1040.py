# Generated by Django 3.0.8 on 2020-08-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_auto_20200819_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkoption',
            name='beer',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='drinkoption',
            name='bottom_only',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='drinkoption',
            name='fullopen',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='drinkoption',
            name='wine',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='drinkoption',
            name='wine_beer',
            field=models.BooleanField(),
        ),
    ]
