# Generated by Django 3.1 on 2020-08-27 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
        ('venues', '0025_auto_20200827_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candles', models.BooleanField()),
                ('sparklers', models.BooleanField()),
                ('indoor_smoking', models.BooleanField()),
                ('designated_smoking_area', models.BooleanField()),
                ('secure_room', models.BooleanField()),
                ('people_per_table', models.IntegerField()),
                ('provide_booster_seats', models.BooleanField()),
                ('provide_place_cards', models.BooleanField()),
                ('ceremony_reception_seperate_rooms', models.BooleanField()),
                ('ceremony_seating_provided', models.BooleanField()),
                ('tip_included', models.BooleanField()),
                ('coat_room', models.BooleanField()),
                ('wheelchair_accessible', models.BooleanField()),
                ('other_notes', models.TextField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.RemoveField(
            model_name='corkfee',
            name='limitation',
        ),
        migrations.RemoveField(
            model_name='paymentplan',
            name='limitation',
        ),
        migrations.RemoveField(
            model_name='photovideo',
            name='limitation',
        ),
        migrations.RemoveField(
            model_name='tasting',
            name='limitation',
        ),
        migrations.RemoveField(
            model_name='weddingcake',
            name='cake',
        ),
        migrations.DeleteModel(
            name='Limitation',
        ),
    ]
