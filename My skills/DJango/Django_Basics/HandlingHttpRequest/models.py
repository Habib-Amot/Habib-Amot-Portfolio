from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(User):
    profile_picture = models.FileField(upload_to='media/images')
