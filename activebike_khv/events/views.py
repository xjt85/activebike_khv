import json
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from datetime import date

# from .forms import CommentForm, PostForm
from .models import About, Article, Event, Link, Report, Route, User, Ip

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetHistoryRequest
from decouple import config

API_ID = config('TLG_API_ID')
API_HASH = config('TLG_API_HASH')
USERNAME = config('TLG_USERNAME')
SESSION_STRING = config('TLG_SESSION_STRING')
TLG_CHANNEL_URL = config('TLG_CHANNEL_URL')

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

all_messages = []   # список всех сообщений


async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 3   # максимальное число записей, передаваемых за один раз

    total_messages = 0
    total_count_limit = 3  # поменяйте это значение, если вам нужны не все сообщения

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
            if message.message == "":
                total_count_limit += 1
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break


async def main():
    url = TLG_CHANNEL_URL
    channel = await client.get_entity(url)
    await dump_all_messages(channel)


with client:
    res = client.loop.run_until_complete(main())


# Метод для получения айпи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip


@cache_page(60 * 2)
def main_page(request):
    template = 'main.html'
    events = Event.objects.all()
    nearest_event = events.filter(date_planned__gt=date.today()).last()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'events': events,
        'nearest_event': nearest_event,
        'all_messages': all_messages
    }
    return render(request, template, context)


@cache_page(60 * 2)
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
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        event.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        event.views.add(Ip.objects.get(ip=ip))
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)


@cache_page(60 * 2)
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
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        article.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        article.views.add(Ip.objects.get(ip=ip))
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)
    context = {
        'article': article,
    }
    return render(request, template, context)


@cache_page(60 * 2)
def reports_index(request):
    template = 'reports/index.html'
    reports = Report.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'reports': reports
    }
    return render(request, template, context)


def report_detail(request, report_id):
    template = 'reports/report_detail.html'
    report = get_object_or_404(Report, pk=report_id)
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        report.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        report.views.add(Ip.objects.get(ip=ip))
    
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)
    context = {
        'report': report,
    }
    return render(request, template, context)


@cache_page(60 * 2)
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
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        route.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        route.views.add(Ip.objects.get(ip=ip))
    # comments = Comment.objects.filter(event=event)
    # author = event.author
    # author_events_count = Event.objects.filter(author=event.author).count()
    # form = CommentForm(request.POST or None)
    context = {
        'route': route,
        'data':json.dumps(route.polyline)
    }
    return render(request, template, context)


@cache_page(60 * 2)
def about_page(request):
    template = 'about.html'
    about_page = About.objects.all()
    links = Link.objects.all()
    # posts = Post.objects.select_related('group')
    # paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'about_page': about_page,
        'links': links
    }
    return render(request, template, context)