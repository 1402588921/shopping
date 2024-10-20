from django.urls import path
from app3 import views


urlpatterns = [
    path('vars/', views.var),
    path('test_control/<int:age>/', views.test_control),
    path('for_label/', views.for_label),
    path('filter/', views.filter),
    path('html_filter/', views.html_filter),
    path('custom_filter/', views.custom_filter),
    path('custom_tags/', views.custom_tags),
    path('show_info_tag/', views.show_info_tag),
    path('welcome/', views.welcome),
]
