from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import (About, Article, Event, EventType, Link, Report,
                     Route, ImageAlbum, Image, SurfaceType, Tag, Ip)


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'author', 'date_planned', 'date_pub', 'date_edit')
    search_fields = ('title',)
    list_filter = ('date_planned',)
    empty_value_display = '-пусто-'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('album', 'name', 'default')
    list_editable = ('default',)
    empty_value_display = '-пусто-'


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'images_count')
    empty_value_display = '-пусто-'


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'url', 'description')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
    empty_value_display = '-пусто-'
    # inlines = [ImageInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'style': 'max-height: 500px;'})}
    }

    class Meta:
        model = Route

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Tag)
admin.site.register(SurfaceType)
admin.site.register(About)
admin.site.register(Ip)
# admin.site.register(Image)
# admin.site.register(ImageAlbum)
