from django.contrib import admin
from .models import EventType, Event

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    search_fields = ('description',)
    empty_value_display = '-пусто-'

class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'caption', 'event_type', 'author', 'date_pub', 'date_planned', 'date_edited')
    list_editable = ('event_type',)
    search_fields = ('description',)
    list_filter = ('date_planned',)
    empty_value_display = '-пусто-'


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
