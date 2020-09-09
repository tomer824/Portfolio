# Generated by Django 3.1 on 2020-09-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200907_1404'),
        ('venues', '0048_auto_20200908_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue'),
        ),
    ]
