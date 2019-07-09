# Generated by Django 2.2 on 2019-07-09 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charmi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Jugadores',
            new_name='Jugador',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Date_Born',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Date_joined',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Last_join',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Last_name',
        ),
        migrations.AlterField(
            model_name='game',
            name='IdGame',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Id_Game', to='charmi.Game_list'),
        ),
        migrations.DeleteModel(
            name='Opponents',
        ),
    ]
