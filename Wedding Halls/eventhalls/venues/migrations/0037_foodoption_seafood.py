# Generated by Django 3.1 on 2020-09-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0036_auto_20200903_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodoption',
            name='seafood',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
