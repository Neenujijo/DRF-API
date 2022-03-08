from django.utils import timezone
from django.db import models
from django.conf import settings
import jwt
from datetime import datetime,timedelta


# Create your models here.

class EmplyeeRegistration(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    employee_code=models.CharField(max_length=300)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
                                                                     
    def __str__(self):
        return self.first_name

    
    @property
    def token(self):
        token=jwt.encode(
            {'username':self.username,'email':self.email,
            'exp':datetime.utcnow()+timedelta(hours=24)},
            settings.SECRET_KEY,algorithm='HS256')
        return token
           

class EmployeeProfile(models.Model):
    employee_designation=models.CharField(max_length=100)
    employee_department=models.CharField(max_length=50)
    dob=models.DateField(max_length=8)
    gender=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=50)
    employee = models.ForeignKey(EmplyeeRegistration, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.employee_designation


class EmployeeSkills(models.Model):
    skill=models.CharField(max_length=50)
    # profile=models.ManyToManyField(EmployeeProfile)
    employee = models.ForeignKey(EmplyeeRegistration, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.skill
