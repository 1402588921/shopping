from django.shortcuts import render
from django.http import HttpRequest


def var(request: HttpRequest):
    lists = ['Java', 'Python', 'C', 'C#', 'JavaScript']
    dicts = dict(name='张三', age=18, sex='男')
    return render(request, '3/var.html', dict(lists=lists, dicts=dicts))


def test_control(request: HttpRequest, age: int):
    lists = ['张飞', '关羽']
    return render(request, '3/test_control.html', dict(age=age, lists=lists))
