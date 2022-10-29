# Generated by Django 3.2.9 on 2022-10-29 04:51

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_rename_gpx_route_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='track',
            field=models.FileField(blank=True, null=True, upload_to=events.models.user_directory_path),
        ),
    ]
