# Generated by Django 2.1.1 on 2018-10-05 15:00

from django.db import migrations, models
import weather.models


class Migration(migrations.Migration):
    dependencies = [
        ('weather', '0002_city_cityid'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='populationcount',
            field=models.IntegerField(default=weather.models.my_random_key),
        ),
    ]
