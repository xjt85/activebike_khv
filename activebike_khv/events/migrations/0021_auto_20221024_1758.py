# Generated by Django 3.2.9 on 2022-10-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20221023_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='event',
            name='text_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]