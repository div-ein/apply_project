from django.db import models
from django.utils import timezone

# Create your models here.

class Apply(models.Model):
  name = models.CharField(max_length=10)
  age = models.IntegerField()
  CHOICES = (
    ('FEMALE','여성'),
    ('MALE','남성'),
  )
  sex = models.CharField(max_length=30, choices = CHOICES)
  body = models.TextField()
  pub_date = models.DateTimeField('date published', default = timezone.now)

  def __str__(self):
    return self.name