# Generated by Django 2.1.1 on 2018-10-06 12:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('weather', '0006_auto_20181006_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]
