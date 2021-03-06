# Generated by Django 3.1 on 2020-09-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0041_auto_20200906_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkoption',
            name='beer_only',
        ),
        migrations.RemoveField(
            model_name='drinkoption',
            name='bottom_shelf',
        ),
        migrations.RemoveField(
            model_name='drinkoption',
            name='full_open_bar',
        ),
        migrations.RemoveField(
            model_name='drinkoption',
            name='wine_and_beer',
        ),
        migrations.RemoveField(
            model_name='drinkoption',
            name='wine_only',
        ),
        migrations.AddField(
            model_name='drinkoption',
            name='drink_options',
            field=models.CharField(choices=[('full_open_bar', 'Full Open Bar'), ('bottom_shelf', 'Bottom Shelf Only'), ('wine_and_beer', 'Wine and Beer'), ('wine_only', 'Wine Only'), ('beer_only', 'Beer Only')], default=False, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinkoption',
            name='pricing',
            field=models.ManyToManyField(to='venues.Pricing'),
        ),
    ]
