# Generated by Django 3.0.8 on 2020-08-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200812_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
