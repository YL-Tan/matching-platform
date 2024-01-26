from django.contrib import admin
from .models import UserProfile, Project, Category, ProjectView

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'bio', 'avatar'] 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'start_date', 'end_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at'] 

@admin.register(ProjectView)
class ProjectViewAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'viewed_at'] 