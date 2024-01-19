from django.db import models
from djongo import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    interests = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    industry = models.CharField(max_length=100)

