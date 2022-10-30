from django.contrib import admin

from .models import (About, Article, Event, EventType, Link, Media, Report,
                     Route, SurfaceType, Tag)


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'author', 'date_planned', 'date_pub', 'date_edit')
    list_editable = ('event_type',)
    search_fields = ('title',)
    list_filter = ('date_planned',)
    empty_value_display = '-пусто-'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
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
    list_display = ('title', 'description', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
    empty_value_display = '-пусто-'
    
    def save_model(self, request, obj, form, change):
            obj.author = request.user
            obj.save()


admin.site.register(Tag)
admin.site.register(SurfaceType)
admin.site.register(Media)
admin.site.register(About)
