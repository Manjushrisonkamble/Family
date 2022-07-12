from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    education = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)


