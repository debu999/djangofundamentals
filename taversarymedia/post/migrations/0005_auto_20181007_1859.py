# Generated by Django 2.1.1 on 2018-10-07 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0004_auto_20181007_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='createdate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]