import typing
from django import template


register = template.Library()


@register.simple_tag
def max_len(value: typing.Any, n: int):
    if len(value) > n:
        return value[0: n]
    else:
        return value


@register.inclusion_tag('3/show_info_tags.html')
def show_info_tags():
    warrior = ['张飞', '关羽', '赵云']
    return dict(warrior=warrior)
