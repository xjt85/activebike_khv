from django import template
from django.db.models import Count
from django.views.decorators.cache import cache_page

from ..models import Article, Link


register = template.Library()


# @cache_page(60 * 10)
@register.inclusion_tag("includes/right_sidebar.html")
def show_sidebar():
    articles = Article.objects.all().annotate(tot_views=Count('views')).order_by('-tot_views')[:2]
    links = Link.objects.all()
    return {
        'popular_articles': articles,
        'links': links
    }
