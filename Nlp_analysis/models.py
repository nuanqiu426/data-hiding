from django.db import models

# Create your models here.

class Uw(models.Model):
    uword=models.CharField(max_length=500)
    utime = models.CharField(max_length=100)
