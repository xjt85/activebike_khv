from django import template
from django.views.decorators.cache import cache_page

from ..models import Article, Link


register = template.Library()


# @cache_page(60 * 10)
@register.inclusion_tag("includes/right_sidebar.html")
def show_sidebar():
    articles = Article.objects.all()
    links = Link.objects.all()
    return {
        'popular_articles': articles,
        'links': links
        }
