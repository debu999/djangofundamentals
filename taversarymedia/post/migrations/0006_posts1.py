# Generated by Django 2.1.1 on 2018-10-07 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0005_auto_20181007_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('createdate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Posts1',
            },
        ),
    ]