from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WeightModel(models.Model):
    weight = models.FloatField(name='weight', null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users')
    date = models.DateField()

