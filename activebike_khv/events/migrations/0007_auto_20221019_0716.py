# Generated by Django 3.2.9 on 2022-10-18 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20221019_0709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['title'], 'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['title'], 'verbose_name': 'Медиа', 'verbose_name_plural': 'Медиа'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'ordering': ['title'], 'verbose_name': 'Маршрут', 'verbose_name_plural': 'Маршруты'},
        ),
    ]
