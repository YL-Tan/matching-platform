from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Project
from .serializers import UserProfileSerializer, ProjectSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def projects(request):
    return render(request, 'projects.html')

def dashboard(request):
    return render(request, 'dashboard.html')
