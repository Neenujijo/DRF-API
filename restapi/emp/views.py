from rest_framework import permissions
from rest_framework import viewsets
from .models import EmployeeProfile, EmployeeSkills, EmplyeeRegistration
from .serializers import UserRegisterSerializer,EmployeeProfileSerializer,EmployeeSkillSerializer


class RegisterView(viewsets.ModelViewSet):# create rest_framework views
    queryset = EmplyeeRegistration.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeProfileView(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


   
class EmployeeSkillsView(viewsets.ModelViewSet):
    queryset = EmployeeSkills.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = [permissions.IsAuthenticated]



