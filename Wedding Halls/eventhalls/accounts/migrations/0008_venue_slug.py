# Generated by Django 3.1 on 2020-09-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='slug',
            field=models.SlugField(default=False),
            preserve_default=False,
        ),
    ]
