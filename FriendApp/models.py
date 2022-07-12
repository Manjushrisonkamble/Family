from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    years = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    position = models.CharField(max_length=200)