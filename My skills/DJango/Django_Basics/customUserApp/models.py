from django.db import models
from django.contrib.auth.models import AbstractUser
from AuthenticationAndAuthorization.validators import VALIDATECHARACTERS
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or Minimum of 4 characters. Letters, digits and spaces are allowed.',
        validators=[VALIDATECHARACTERS, MinLengthValidator(4), MaxLengthValidator(150)],
        error_messages={
            'unique': "A user with that username already exists.",
            'max_length': "Username must be less than 150 characters.",
            'min_length': "Username must be at least 4 characters long."
        }
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='users',
        related_query_name='users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='users',
        related_query_name='users'
    )
