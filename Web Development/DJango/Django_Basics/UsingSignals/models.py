from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# defining a user profile model that will be used to store the profile data of any particular user
# this will be linked automatically to all newly created users of our website

class UserProfile(models.Model):
    bio = models.TextField(blank=True)
    profile_link = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=250, blank=True)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
