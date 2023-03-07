from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

# helper functions
def user_directory_path(instance, filename:str):
    return f"user_{instance.id}/img/{filename}"

# custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Super User should be staff member")
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Super User should be superuser")

        return self.create_user(email=email,password=password, **kwargs)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username=models.CharField(max_length=50)
    pic_avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    objects=CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __str__(self):
        
        return self.username

