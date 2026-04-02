from django import template

register = template.Library()


@register.filter(name='split')
def split_filter(value, arg):
    """Split a string by the given delimiter."""
    return value.split(arg)
