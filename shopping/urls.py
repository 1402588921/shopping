from django.contrib import admin
from django.urls import path, include
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', include('app2.urls')),
    path('', include('app3.urls')),
]
