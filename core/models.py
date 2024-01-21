from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    interests = models.TextField()
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.png')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.title
