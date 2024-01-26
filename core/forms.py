from django import forms
from .models import UserProfile, Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.conf import settings

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['company_name', 'email', 'interests', 'bio', 'avatar', 'website']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'start_date', 'end_date', 'budget', 'tags', 'location', 'investment_sought', 'contact_email']