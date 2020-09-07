# Generated by Django 3.1 on 2020-09-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
        ('venues', '0037_foodoption_seafood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodoption',
            name='chicken_and_fish',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='fish_meal',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='lamb_meal',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='meat_and_chicken',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='meat_and_fish',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='meat_meal',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='seafood',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='vegan',
        ),
        migrations.RemoveField(
            model_name='foodoption',
            name='vegitarian',
        ),
        migrations.AddField(
            model_name='foodoption',
            name='description_of_food',
            field=models.CharField(default=False, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodoption',
            name='name_of_food',
            field=models.CharField(default=False, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodoption',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue'),
        ),
    ]
