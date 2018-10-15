# Generated by Django 2.1.1 on 2018-10-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(
                choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player Wins'),
                         ('L', 'First Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
