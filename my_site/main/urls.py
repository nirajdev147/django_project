# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),     # Root homepage (127.0.0.1:8000/)
    path('main/', views.home, name='home'),  # Members List page (127.0.0.1:8000/main/)
    path('main/details/<int:id>', views.details, name='details'),   # Details Page
    path('testing/', views.testing, name = 'testing'),  #sandbox test page
    path('index/', views.index, name = 'index')  #index page
]
