from django.contrib import admin
from .models import UserProfile, Project

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'bio', 'avatar'] 

admin.site.register(Project)