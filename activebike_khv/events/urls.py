from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_index, name='events_index'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
]
