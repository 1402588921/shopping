import datetime
from django.shortcuts import render
from django.http import HttpRequest


def var(request: HttpRequest):
    lists = ['Java', 'Python', 'C', 'C#', 'JavaScript']
    dicts = dict(name='张三', age=18, sex='男')
    return render(request, '3/var.html', dict(lists=lists, dicts=dicts))


def test_control(request: HttpRequest, age: int):
    lists = ['张飞', '关羽']
    return render(request, '3/test_control.html', dict(age=age, lists=lists))


def for_label(request: HttpRequest):
    dict1 = dict(name='Django开发', price=80, author='张三')
    dict2 = dict(name='Python开发', price=90, author='李四')
    dict3 = dict(name='Java开发', price=100, author='王五')
    lists = [dict1, dict2, dict3]
    return render(request, '3/for_label.html', dict(lists=lists))


def filter(request: HttpRequest):
    s1 = 'abcdefg'
    s2 = 'ABCDEFG'
    slice_str = '01234567890'
    time_str = datetime.datetime.now()
    return render(request, '3/filter.html', dict(
        s1=s1, s2=s2, slice_str=slice_str, time_str=time_str
    ))


def html_filter(request: HttpRequest):
    table = '<table border=1><tr><td>我是一个表格</table></tr></td>'
    script = ("<script language='javascript'>"
              "document.write('过来了还是可以的');</script>")
    return render(request, '3/html_filter.html', dict(
        table=table, script=script
    ))


def custom_filter(request: HttpRequest):
    warrior = ['张飞', '关羽', '赵云']
    return render(request, '3/custom_filter.html', dict(warrior=warrior))
