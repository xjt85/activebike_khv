from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.main_page, name='main_page'),

    path('events/', views.events_index, name='events_index'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),

    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    path('routes/', views.routes_index, name='routes_index'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('routes/<int:route_id>/map/', views.route_map, name='route_map'),

    path('reports/', views.reports_index, name='reports_index'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),

    path('about/', views.about_page, name='about_page'),
]
