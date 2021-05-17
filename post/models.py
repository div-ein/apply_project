from django.db import models
from django.utils import timezone

# Create your models here.

class Apply(models.Model):
  name = models.CharField(max_length=10)
  age = models.IntegerField()
  sex = models.CharField(max_length=5)
  body = models.TextField()
  pub_date = models.DateTimeField('date published', default = timezone.now)

  def __str__(self):
    return self.name