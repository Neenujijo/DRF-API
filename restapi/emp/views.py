from django.shortcuts import render
from .models import emplyee_usereg
from .serializers import  UserRegisterSerializer,LoginSerializer
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.http import Http404




# Create your views here.

class RegisterView(APIView):# create rest_framework views
    
    def post(self,request):
        #write data
        #using serializer for validating data.
        serializer=UserRegisterSerializer(data=request.data)# pass the data directly to serialiser,when data get from db.

        # check to validate
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(APIView):

    def get(self,request):
        employees=emplyee_usereg.objects.all()
        serializer=UserRegisterSerializer(employees,many=True)
        return Response(serializer.data)
        


class LoginAPIView(APIView):

    def post(self, request):
      
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"status": "successfully login",}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return Response({"status": "successfully logout",},status=status.HTTP_200_OK)



class EmployeeDetailsView(APIView):
    """
    Retrieve, update or delete .
    """
    def get_object(self, pk):
        try:
            return emplyee_usereg.objects.get(pk=pk)
        except emplyee_usereg.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = UserRegisterSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = UserRegisterSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)