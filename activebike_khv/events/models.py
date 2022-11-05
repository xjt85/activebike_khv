from tabnanny import verbose
import gpxpy
import gpxpy.gpx
import polyline
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
# from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import SET_NULL
from markdown import markdown

User = get_user_model()


class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)
    date_edit = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.ip


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


class EventType(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    text_html = models.TextField(blank=True, editable=False)
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
    views = models.ManyToManyField(Ip, related_name="events_views", blank=True)

    class Meta:
        ordering = ['-date_planned']
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title[:30]

    def save(self):
        self.text_html = markdown(self.text)
        super(Event, self).save()

    def total_views(self):
        return self.views.count()


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='articles/',
        blank=True
    )
    text = models.TextField(blank=True)
    text_html = models.TextField(blank=True, editable=False)
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
    views = models.ManyToManyField(Ip, related_name="articles_views", blank=True)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title[:30]

    def save(self):
        self.text_html = markdown(self.text)
        super(Article, self).save()

    def total_views(self):
        return self.views.count()


class Report(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='reports/',
        blank=True
    )
    text = models.TextField(blank=True)
    text_html = models.TextField(blank=True, editable=False)
    tags = models.ManyToManyField(
        Tag,
        related_name='reports',
        verbose_name='Теги',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(Ip, related_name="reports_views", blank=True)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return self.title[:30]

    def save(self):
        self.text_html = markdown(self.text)
        super(Report, self).save()

    def total_views(self):
        return self.views.count()


def user_directory_path(instance, filename):
    return 'routes/user_{0}/{1}'.format(instance.author.id, filename)


class Route(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(
        'Картинка',
        upload_to='routes/',
        blank=True
    )
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name="ссылка (если есть)")
    track = models.FileField(upload_to=user_directory_path, null=True, blank=True, verbose_name="GPX-трек (если имеется)")
    polyline = models.TextField(blank=True, editable=False, verbose_name="Полилиния (необязательно)")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='routes',
        verbose_name="Автор"
    )
    type = models.ForeignKey(
        EventType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='routes',
        verbose_name="Тип активности"
    )
    length = models.IntegerField(default=0, blank=True, verbose_name="Дистанция, км")
    height_gain = models.IntegerField(default=0, blank=True, verbose_name="Набор высоты, м")
    surface_type = models.ForeignKey(
        SurfaceType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='routes',
        verbose_name="Покрытие"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    tags = models.ManyToManyField(
        Tag,
        related_name='routes',
        verbose_name='Теги',
        blank=True,
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(Ip, related_name="routes_views", blank=True)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.title[:30]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.track:
            with open(self.track.path, "r", encoding="utf-8") as file:
                gpx = gpxpy.parse(file)
            data = []
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        data.append([float(point.latitude), float(point.longitude)])

            self.polyline = polyline.encode(data)
            super().save(*args, **kwargs)

    def total_views(self):
        return self.views.count()


class Link(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.text[:30]


class Media(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['text']
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    def __str__(self):
        return self.text[:30]


class About(models.Model):
    title = models.CharField(max_length=200)
    markdown_field = models.TextField(blank=True)
    html_field = models.TextField(blank=True, editable=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title[:30]

    def save(self):
        self.html_field = markdown(self.markdown_field)
        super(About, self).save()
