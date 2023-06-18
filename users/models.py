from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="user Email")
    phone = models.CharField(max_length=50, verbose_name="phone number")
    country = models.CharField(max_length=50, verbose_name="user country")
    avatar = models.ImageField(upload_to="images", verbose_name="user avatar", null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


