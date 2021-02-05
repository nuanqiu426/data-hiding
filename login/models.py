from django.db import models

# Create your models here.


class User(models.Model):
    uid=models.CharField(max_length=50, primary_key=True)
    upassword=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    uaddress=models.CharField(max_length=20)
    uemail=models.CharField(max_length=20)
    uflag=models.CharField(max_length=20)


class Whisper(models.Model):
    Now_time = models.CharField(max_length=20, primary_key=True)
    ask = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    Num_plate = models.CharField(max_length=30,default=446146024)
