# Generated by Django 2.1.1 on 2018-09-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(default=0),
        ),
    ]
