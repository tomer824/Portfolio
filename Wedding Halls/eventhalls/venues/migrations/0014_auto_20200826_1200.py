# Generated by Django 3.1 on 2020-08-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
        ('venues', '0013_auto_20200819_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndoorOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indoor_reception', models.BooleanField()),
                ('indoor_ceremony', models.BooleanField()),
                ('indoor_dancing', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='outdooroptions',
            name='venue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='outdooroptions', to='accounts.venue'),
        ),
        migrations.AlterField(
            model_name='venuedetail',
            name='venue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='venuedetail', to='accounts.venue'),
        ),
    ]
