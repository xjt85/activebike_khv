from django.contrib import admin
from .models import EventType, Tag, SurfaceType, Event, Article, Link, Media, Route


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    search_fields = ('description',)
    empty_value_display = '-пусто-'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'date_pub', 'date_edit')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'event_type', 'author', 'date_planned', 'date_pub', 'date_edit')
    list_editable = ('event_type',)
    search_fields = ('description',)
    list_filter = ('date_planned',)
    empty_value_display = '-пусто-'


admin.site.register(Tag)
admin.site.register(SurfaceType)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Link)
admin.site.register(Media)
admin.site.register(Route)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
