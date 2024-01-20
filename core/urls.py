""" This file is a configuration file for defining URL patterns and 
associating them with corresponding view functions in the Django 
application
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]