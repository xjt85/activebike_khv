from django import template
from ..models import Article

register = template.Library()

@register.inclusion_tag("includes/right_sidebar.html")
def show_sidebar():
  articles = Article.objects.all()
  return {'popular_articles': articles}