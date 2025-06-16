from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edicoes/', views.edicoes, name='edicoes'),

    
]