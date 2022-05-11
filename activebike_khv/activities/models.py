from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import SET_NULL

User = get_user_model()

class ActivityType(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Activity(models.Model):
    caption = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='activities/',
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    date_plane = models.DateTimeField(auto_now_add=True)
    date_fact = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now_add=True)
    a_type = models.ForeignKey(
        ActivityType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='activities'
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
