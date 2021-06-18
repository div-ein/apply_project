from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  age = models.IntegerField(blank=True, null=True, default=None)
  # CHOICES = (
  #   ('FEMALE','여성'),
  #   ('MALE','남성'),
  # )
  # sex = models.CharField(max_length=30, choices = CHOICES, blank=True, null=True, default=None)
