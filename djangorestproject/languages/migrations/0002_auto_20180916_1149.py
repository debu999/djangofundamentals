# Generated by Django 2.1.1 on 2018-09-16 11:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['-rank'], 'verbose_name': 'Table: Language'},
        ),
    ]
