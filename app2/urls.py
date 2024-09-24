from django.urls import path
from app2 import views


urlpatterns = [
    path(r'app2/show/(?P<year>\d+)/', views.index)
]
