# Generated by Django 3.0.8 on 2020-08-12 12:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20200812_1153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='Venue',
        ),
    ]
