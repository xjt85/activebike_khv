# Generated by Django 3.2.9 on 2022-12-21 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_link_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['order'], 'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
    ]
