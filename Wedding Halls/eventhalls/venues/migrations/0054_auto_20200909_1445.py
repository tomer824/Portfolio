# Generated by Django 3.1 on 2020-09-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0053_remove_venuedetail_min_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuedetail',
            name='max_guests',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]