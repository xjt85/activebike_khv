from django import template

from core.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }
