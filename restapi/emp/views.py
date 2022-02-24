from django.shortcuts import render
from .models import emplyee_usereg
from .serializers import  UserRegisterSerializer,LoginSerializer
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView




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

        
