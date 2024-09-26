from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from models import UserBaseInfo


def index(request: HttpRequest, year):
    print(request.GET.get('username'))
    return HttpResponse(f'app2 中的 show 方法，参数的值为{year}')


def article_page(request: HttpRequest, page: int, key: str):
    return HttpResponse(f'传入的页数是:{page}，传入的key={key}')


def url_reverse(request: HttpRequest, id: int):
    return render(request, '2/url_reverse.html')


def test_post(request: HttpRequest):
    print(request.method)
    print(request.POST.get('username'))
    return render(request, '2/test_post.html')


def test_response(request: HttpRequest):
    response = HttpResponse()
    response.write('Hello Django')
    response.write('<br>')
    response.write(response.content)
    response.write('<br>')
    response.write(response['content-type'])
    response.write('<br>')
    response.write(response.charset)
    response.write(response.status_code)
    response.write('<br>')
    return response


def test_render(request: HttpRequest):
    return render(
        request,
        '2/test_render.html',
        dict(info='Hello Django'),
        content_type='text/html'
    )


def test_redirect_model(request: HttpRequest, id: int):
    user = UserBaseInfo.objects.get(id=id)


def userinfo(request: HttpRequest, id: int):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse('编号' + str(user.id) + '姓名' + user.username)
