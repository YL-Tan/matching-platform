from django.shortcuts import render, redirect
from .models import UserProfile, Project
from .forms import UserRegisterForm, UserProfileForm, ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home Page View
def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')

# User Profile View
@login_required
def profile(request):
    """
    Handle the user profile page.
    """
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})

# Projects View
def projects(request):
    """
    Display all projects.
    """
    project_list = Project.objects.all()
    return render(request, 'projects.html', {'project_list': project_list})

@login_required
def create_project(request):
    """
    Handle the project creation process.
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})

# Dashboard View
@login_required
def dashboard(request):
    """
    User dashboard showing their projects.
    """
    user_projects = Project.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_projects': user_projects})

# User Login View
def user_login(request):
    """
    Handle the user login process.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html')

# User Logout View
def user_logout(request):
    """
    Handle the user logout process.
    """
    logout(request)
    return redirect('home')

# User Registration View
def register(request):
    """
    Handle the new user registration process.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form.')

    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
