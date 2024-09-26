from django.urls import re_path, path
from app2 import views


urlpatterns = [
    re_path(r'app2/show/(?P<year>\d{4})/', views.index),
    re_path(r'app2/show/(?P<page>\d+)&key=(?P<key>\w+)', views.article_page),
    path(
        'app2/url_reverse/<int:id>', views.url_reverse, name='app2_url_reverse'
    ),
    path('app2/test_post/', views.test_post),
    path('app2/test_response/', views.test_response),
    path('app2/test_render/', views.test_render),
]
