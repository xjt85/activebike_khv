# Generated by Django 3.2.9 on 2022-11-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_ip_date_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='date_edit',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
