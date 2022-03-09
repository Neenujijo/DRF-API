from rest_framework import serializers
from .models import EmployeeProfile,EmployeeSkills



# class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):       
#     class Meta:
#         model=EmplyeeRegistration
#         fields=('id','url','first_name','last_name','employee_code','username','password','email')

    
class EmployeeProfileSerializer(serializers.ModelSerializer):

    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    employee_code=serializers.CharField(max_length=300)
    employee_designation=serializers.CharField(max_length=100)
    employee_department=serializers.CharField(max_length=50)
    dob = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    gender=serializers.CharField(max_length=10)

    class Meta:
        model=EmployeeProfile
        fields=('id','employee','first_name','last_name','employee_code','employee_designation','employee_department')


class EmployeeSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeSkills
        fields = ('id','url','employee','skill')


