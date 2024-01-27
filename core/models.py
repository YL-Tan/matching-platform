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
    preferred_categories = models.ManyToManyField('Category', blank=True)
    preferred_countries = models.ManyToManyField('Country', blank=True)
    investment_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.company_name
    
    def has_sufficient_interactions(self):
        MIN_INTERACTIONS = 3
        interaction_count = ProjectView.objects.filter(user=self.user).count()
        return interaction_count >= MIN_INTERACTIONS

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    investment_sought = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # expected_return = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProjectView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)