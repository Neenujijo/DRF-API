from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

# class EmplyeeRegistration(models.Model):

#     
#     
#     
#     username=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)
#     email=models.EmailField(max_length=30)
                                                                     
#     def __str__(self):
#         return self.first_name

    
    # @property
    # def token(self):
    #     token=jwt.encode(
    #         {'username':self.username,'email':self.email,
    #         'exp':datetime.utcnow()+timedelta(hours=24)},
    #         settings.SECRET_KEY,algorithm='HS256')
    #     return token
           

class EmployeeProfile(models.Model):
    first_name=models.CharField(max_length=100,null=True, blank=True)
    last_name=models.CharField(max_length=100,null=True, blank=True)
    employee_code=models.CharField(max_length=300, null=True, blank=True)
    employee_designation=models.CharField(max_length=100,null=True, blank=True)
    employee_department=models.CharField(max_length=50,null=True, blank=True)
    dob=models.DateField(max_length=8,null=True, blank=True)
    gender=models.CharField(max_length=10,null=True, blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.employee


class EmployeeSkills(models.Model):
    skill=models.CharField(max_length=50)
    # profile=models.ManyToManyField(EmployeeProfile)
    employee = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.employee
