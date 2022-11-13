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
from django.template.defaultfilters import slugify


User = get_user_model()


class Ip(models.Model):  # наша таблица где будут айпи адреса
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


# ---------------------------- НОВАЯ СТРУКТУРА -----------------------------------------------------


def get_image_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_image_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    # album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


class ImageAlbum(models.Model):
    images = models.ForeignKey(Image, related_name='images', on_delete=models.CASCADE)

    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    text_html = models.TextField(blank=True, editable=False)
    album = models.OneToOneField(ImageAlbum, related_name='image_album', on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True
    )
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(Ip, blank=True, editable=False)


class Event(Post):
    image = models.ImageField(
        'Картинка',
        upload_to='events/',
        blank=True
    )
    event_type = models.ForeignKey(
        EventType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='events'
    )
    author = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        null=True,
        related_name='posts'
    )
    date_planned = models.DateTimeField()

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


class Article(Post):
    image = models.ImageField(
        'Картинка',
        upload_to='articles/',
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        null=True,
        related_name='articles'
    )

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


# ---------------------------------------------------------------------------------


class Report(Post):
    image = models.ImageField(
        'Картинка',
        upload_to='reports/',
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
    )

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


def get_height_gain(gpx_data_array):
    result = 0
    for i in range(len(gpx_data_array) - 1):
        z1 = gpx_data_array[i][2]
        z2 = gpx_data_array[i + 1][2]
        if z2 > z1:
            result += z2 - z1
    return result


class Route(Post):
    image = models.FileField(blank=True, upload_to='routes/images', verbose_name="Скрин маршрута")
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name="ссылка на трек (необязательно)")
    track = models.FileField(upload_to=user_directory_path, null=True, blank=True, verbose_name="GPX-трек (необязательно)")
    polyline = models.TextField(blank=True, editable=False, verbose_name="Полилиния (генерируется автоматически при загрузке трека GPX)")
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
    length = models.FloatField(default=0, null=True, verbose_name="Дистанция, км")
    height_gain = models.PositiveSmallIntegerField(default=0, null=True, verbose_name="Набор высоты, м")
    surface_type = models.ForeignKey(
        SurfaceType,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='routes',
        verbose_name="Покрытие"
    )

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.title[:30]

    def save(self, *args, **kwargs):
        self.text_html = markdown(self.text)
        # super(Route, self).save()
        super().save(*args, **kwargs)

        if self.track:
            with open(self.track.path, "r", encoding="utf-8") as file:
                gpx = gpxpy.parse(file)

            data = []
            polyline_data = []

            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        data.append([float(point.latitude), float(point.longitude), point.elevation])
                        polyline_data.append([float(point.latitude), float(point.longitude)])

            self.polyline = polyline.encode(polyline_data)

            if self.length == 0:
                self.length = round(gpx.get_moving_data(raw=True).moving_distance / 1000, 1)

            if self.height_gain == 0:
                self.height_gain = get_height_gain(data)

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


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    text_html = models.TextField(blank=True, editable=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title[:30]

    def save(self):
        self.text_html = markdown(self.text)
        super(About, self).save()
