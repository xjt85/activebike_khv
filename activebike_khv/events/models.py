from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import SET_NULL

User = get_user_model()

class EventType(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'

class Event(models.Model):
    caption = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='events/',
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    event_type = models.ForeignKey(
        EventType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='activities'
    )
    date_planned = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption[:15]

    class Meta:
        ordering = ['-date_edited']
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
