# Generated by Django 3.2.9 on 2022-10-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
