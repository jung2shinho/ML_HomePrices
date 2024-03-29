# Generated by Django 4.2.5 on 2023-09-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_rename_firstname_approvals_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=2)),
                ('bathrooms', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('sqft', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Approvals',
        ),
    ]
