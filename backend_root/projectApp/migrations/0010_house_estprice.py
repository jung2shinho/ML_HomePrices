# Generated by Django 4.2.5 on 2023-09-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0009_house_latitude_house_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='estPrice',
            field=models.IntegerField(default=0),
        ),
    ]
