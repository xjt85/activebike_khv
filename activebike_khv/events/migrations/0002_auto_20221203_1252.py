# Generated by Django 3.2.9 on 2022-12-03 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model', to='events.imagealbum', verbose_name='Альбом фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_edit',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата правки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_html',
            field=models.TextField(blank=True, editable=False, verbose_name='отформатированное описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, editable=False, to='events.Ip', verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='route',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='routes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='route',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ссылка на внешний ресурс с треком (необязательно)'),
        ),
    ]
