from rest_framework import serializers
from .models import EmplyeeRegistration,EmployeeProfile,EmployeeSkills



class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
   
        
    class Meta:
        model=EmplyeeRegistration
        fields=('id','url','First_name','Last_name','Emp_code','Username','Password','Email')


    
class EmployeeProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=EmployeeProfile
        fields=('id','url','Employee','Emp_designation','Emp_department','Dob','Gender','Phone_no')



class EmployeeSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeSkills
        fields = ('id','url','Employee','skill')