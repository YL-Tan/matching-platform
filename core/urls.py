""" This file is a configuration file for defining URL patterns and 
associating them with corresponding view functions in the Django 
application
"""
from django.urls import path
from . import web_views, api_views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'userprofiles', api_views.UserProfileViewSet)
router.register(r'projects', api_views.ProjectViewSet)

urlpatterns = [
    path("", web_views.home, name='home'),
    path('profile/', web_views.profile, name='profile'),
    path('projects/', web_views.projects, name='projects'),
    path('create_project/', web_views.create_project, name='create_project'),
    path('dashboard/', web_views.dashboard, name='dashboard'),

    # Authentication URLs
    path('login/', web_views.user_login, name='login'),
    path('logout/', web_views.user_logout, name='logout'),
    path('register/', web_views.register, name='register'),
    
    # Route to the recommendation page
    path('user_recommendations/', web_views.user_recommendations, name='user_recommendations'),
    path('project_details/<int:project_id>/', web_views.project_details, name='project_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
