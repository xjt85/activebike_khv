from multiprocessing import Event
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
import json

# from .forms import CommentForm, PostForm
from .models import User, Event, Article, Route, Link, About


def events_index(request):
    template = 'events/index.html'
    events = Event.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'events': events
    }
    return render(request, template, context)


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)


def articles_index(request):
    template = 'articles/index.html'
    articles = Article.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles
    }
    return render(request, template, context)


def article_detail(request, article_id):
    template = 'articles/article_detail.html'
    article = get_object_or_404(Article, pk=article_id)
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)
    context = {
        'article': article,
    }
    return render(request, template, context)


def routes_index(request):
    template = 'routes/index.html'
    routes = Route.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'routes': routes
    }
    return render(request, template, context)


def route_detail(request, route_id):
    template = 'routes/route_detail.html'
    route = get_object_or_404(Route, pk=route_id)
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)
    context = {
        'route': route,
        'data':json.dumps(route.polyline)
    }
    return render(request, template, context)


def links_index(request):
    template = 'links/index.html'
    links = Link.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'links': links
    }
    return render(request, template, context)


def about_page(request):
    template = 'about.html'
    about_page = About.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'about_page': about_page
    }
    return render(request, template, context)