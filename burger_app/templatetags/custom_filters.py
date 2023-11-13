from django import template
register = template.Library()


@register.filter(name='filter_by_price_range')
def filter_by_price_range(burgers, price_range):
    min_price, max_price = map(int, price_range.split(':'))
    return [burger for burger in burgers if min_price <= burger.price <= max_price]



@register.filter(name='filter_by_special_ingredient')
def filter_by_special_ingredient(burgers, ingredient_name):
    return [burger for burger in burgers if burger.ingredients.filter(name=ingredient_name).exists()]