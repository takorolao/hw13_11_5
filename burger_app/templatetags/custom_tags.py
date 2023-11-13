import random
from django import template
from burger_app.models import Burger
from burger_app.models import Ingredient

register = template.Library()

@register.simple_tag
def random_burger():
    return random.choice(Burger.objects.all())


@register.simple_tag
def ingredient_count():
    return Ingredient.objects.count()