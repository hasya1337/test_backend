from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}

    active_url = request.path
    active_item = None

    # Поиск активного пункта меню
    for item in menu.items.all():
        if item.get_url() == active_url:
            active_item = item
            break

    return {
        'menu': menu,
        'active_item': active_item
    }
