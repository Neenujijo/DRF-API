# from django.utils import timezone
from django.db import models
import jwt
from datetime import datetime,timedelta

from django.conf import settings

# Create your models here.

class emplyee_usereg(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dob=models.DateField(max_length=8)
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=50)


    def __str__(self):
        return self.first_name

