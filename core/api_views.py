from .serializers import UserProfileSerializer, ProjectSerializer
from rest_framework import viewsets
from .models import UserProfile, Project


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
