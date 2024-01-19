""" This file is a configuration file for defining URL patterns and 
associating them with corresponding view functions in the Django 
application
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home')
]