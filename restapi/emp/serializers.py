from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from .models import EmplyeeRegistration,EmployeeProfile,EmployeeSkills



class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):       
    class Meta:
        model=EmplyeeRegistration
        fields=('id','url','first_name','last_name','employee_code','username','password','email')

    
class EmployeeProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=EmployeeProfile
        fields=('id','url','employee','employee_designation','employee_department','dob','gender','phone_number')


class EmployeeSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeSkills
        fields = ('id','url','employee','skill')


