from django import template
from pizzaapp.models import Categories

register = template.Library()


@register.inclusion_tag('pizzaapp/list_of_categories.html')
def get_categories():
    categories = Categories.objects.all()
    return {'categories': categories}
