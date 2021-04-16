from django import template

register = template.Library()

@register.simple_tag()
def check(a, b):
    pass