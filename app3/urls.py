from django.urls import path
from app3 import views


urlpatterns = [
    path('vars/', views.var),
    path('test_control/<int:age>', views.test_control),
]
