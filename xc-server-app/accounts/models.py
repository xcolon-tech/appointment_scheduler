from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, blank=False, null=False)