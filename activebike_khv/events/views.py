from multiprocessing import Event
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

# from .forms import CommentForm, PostForm
from .models import EventType, Event, User

def index(request):
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

