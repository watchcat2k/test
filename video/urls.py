from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.video_index),
    path('register', views.user_register),
    path('avatar', views.user_avatar)
]