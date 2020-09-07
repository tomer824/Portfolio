# Generated by Django 3.1 on 2020-09-06 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
        ('venues', '0040_auto_20200906_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodoption',
            name='pricing',
            field=models.ManyToManyField(to='venues.Pricing'),
        ),
        migrations.AddField(
            model_name='foodoption',
            name='venue',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.venue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodoption',
            name='meal_option',
            field=models.BooleanField(choices=[(True, 'Sit Down'), (False, 'Buffet')]),
        ),
        migrations.DeleteModel(
            name='MealOption',
        ),
    ]
