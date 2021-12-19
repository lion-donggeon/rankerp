from django import template

register = template.Library()


@register.filter
def sub(value, arg):

    print("value {}  - arg   {}   = {} ".format(value, arg,(value-arg)))
    return value - arg
