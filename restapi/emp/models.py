# from django.utils import timezone
from django.db import models


# Create your models here.

class EmplyeeRegistration(models.Model):

    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Emp_code=models.CharField(max_length=300)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Email=models.EmailField(max_length=30)
    
    
                                                                    
    def __str__(self):
        return self.First_name


class EmployeeProfile(models.Model):
    Emp_designation=models.CharField(max_length=100)
    Emp_department=models.CharField(max_length=50)
    Dob=models.DateField(max_length=8)
    Gender=models.CharField(max_length=10)
    Phone_no=models.CharField(max_length=50)
    Employee = models.ForeignKey(EmplyeeRegistration, on_delete=models.CASCADE,null=True)
    
    

    def __str__(self):
        return self.Emp_designation


class EmployeeSkills(models.Model):
    skill=models.CharField(max_length=50)
    # profile=models.ManyToManyField(EmployeeProfile)
    Employee = models.ForeignKey(EmplyeeRegistration, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.skill
