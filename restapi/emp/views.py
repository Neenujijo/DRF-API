from django.shortcuts import render
from rest_framework import viewsets
from .models import EmployeeProfile, EmployeeSkills, EmplyeeRegistration
from .serializers import UserRegisterSerializer,EmployeeProfileSerializer,EmployeeSkillSerializer



class RegisterView(viewsets.ModelViewSet):# create rest_framework views
    queryset = EmplyeeRegistration.objects.all()
    serializer_class = UserRegisterSerializer



class EmployeeProfileView(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

   
class EmployeeSkillsView(viewsets.ModelViewSet):
    queryset = EmployeeSkills.objects.all()
    serializer_class = EmployeeSkillSerializer
