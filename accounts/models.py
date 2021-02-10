from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)