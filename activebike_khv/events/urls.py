from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_index, name='events_index'),
    path('events/', views.events_index, name='events_index'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
]
