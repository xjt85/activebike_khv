# Generated by Django 3.2.9 on 2022-11-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0030_alter_route_polyline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='events_views', to='events.Ip'),
        ),
    ]
