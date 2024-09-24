from django.http import HttpResponse


def index(request, year):
    return HttpResponse(f'app2 中的 show 方法，参数的值为{year}')
