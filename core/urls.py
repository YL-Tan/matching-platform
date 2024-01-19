""" This file is a configuration file for defining URL patterns and 
associating them with corresponding view functions in the Django 
application
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('dashboard/', views.dashboard, name='dashboard'),
]