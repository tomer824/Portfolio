# Generated by Django 3.1 on 2020-08-27 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_discount'),
        ('venues', '0022_auto_20200827_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
    ]