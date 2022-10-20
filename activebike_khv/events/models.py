from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import SET_NULL

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Название тега')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class SurfaceType(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Тип покрытия')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тип дорожного покрытия'
        verbose_name_plural = 'Типы дорожных покрытий'

    def __str__(self):
        return self.name


class RouteType(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Имя')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тип маршрута'
        verbose_name_plural = 'Типы маршрутов'

    def __str__(self):
        return self.name


class EventType(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'


class Event(models.Model):
    title = models.CharField(max_length=200)
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
        related_name='events'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='events',
        verbose_name='Теги',
        blank=True,
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    date_planned = models.DateTimeField()

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['-date_planned']
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='articles/',
        blank=True
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='articles',
        verbose_name='Теги',
        blank=True,
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Report(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='reports/',
        blank=True
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='reports',
        verbose_name='Теги',
        blank=True,
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


class Link(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text[:30]

    class Meta:
        ordering = ['text']
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Media(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:30]

    class Meta:
        ordering = ['text']
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class Route(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='routes'
    )
    type = models.ForeignKey(
        RouteType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='routes'
    )
    length = models.IntegerField(null=True)
    height_gain = models.IntegerField(null=True)
    surface_type = models.ForeignKey(
        SurfaceType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='routes'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='routes',
        verbose_name='Теги'
    )
    url = models.CharField(max_length=200, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['title']
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
