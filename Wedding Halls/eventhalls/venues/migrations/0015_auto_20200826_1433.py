# Generated by Django 3.1 on 2020-08-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0014_auto_20200826_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overnight',
            name='hotel_partners',
            field=models.TextField(),
        ),
    ]