from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserModelManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email must be provided")
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        assert kwargs.get('is_superuser') == True, "admin property must be set to true"
        assert kwargs.get('is_staff') == True, "admin must be an active member of this application"

        return self.create_user(email=email, password=password, **kwargs)




class UserModel(AbstractUser):
    email = models.EmailField(unique=True, primary_key=True)
    mfa_enabled = models.BooleanField(default=False)
    mfa_secrete = models.CharField(max_length=100, unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserModelManager()
