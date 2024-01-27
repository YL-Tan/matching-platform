from .serializers import UserProfileSerializer, ProjectSerializer
from rest_framework import viewsets
from .models import UserProfile, Project
from .forms import UserProfileForm
from .utils import extract_features, create_user_vector, calculate_similarity
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

class RecommendationViewSet(viewsets.ViewSet):
    """
    API endpoint for recommendations.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user_profile = UserProfile.objects.get(user=request.user)

        user_preferences = {
            'preferred_categories': user_profile.preferred_categories,
            'preferred_countries': user_profile.preferred_countries,
        }

        tfidf_matrix, vectorizer = extract_features()
        # print("TF-IDF Matrix Shape:", tfidf_matrix.shape)
        user_vector = create_user_vector(user_preferences, vectorizer)
        # print("User Vector:", user_vector)
        similarity_scores = calculate_similarity(tfidf_matrix, user_vector)
        # print("Similarity Scores:", similarity_scores)

        # Check if similarity_scores is 1D or 2D and adjust accordingly
        if len(similarity_scores.shape) == 1:
            # For 1D array
            ranked_project_indices = similarity_scores.argsort()[::-1].tolist()
        else:
            # For 2D array (existing logic)
            ranked_project_indices = similarity_scores.argsort()[0][::-1].tolist()
        # print("Ranked Project Indices:", ranked_project_indices)
        top_project_indices = ranked_project_indices[:5]
        print("Top Project Indices:", top_project_indices)
        recommended_projects = [Project.objects.all()[index] for index in top_project_indices]
        # Serialize and return the recommended projects
        serialized_projects = ProjectSerializer(recommended_projects, many=True)
        return Response({'recommendations': serialized_projects.data})