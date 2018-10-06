# Generated by Django 2.1.1 on 2018-09-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('guestbook', '0003_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='language',
            field=models.ManyToManyField(to='guestbook.Language'),
        ),
    ]
