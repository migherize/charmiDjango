# Generated by Django 2.2 on 2019-07-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charmi', '0002_auto_20190712_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='ruta',
            field=models.ImageField(upload_to='../imagenes/Profiles/'),
        ),
    ]