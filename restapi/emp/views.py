from rest_framework import permissions
from django.shortcuts import render,get_object_or_404
# from rest_framework import viewsets
from .models import EmployeeProfile, EmployeeSkills
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User=get_user_model()


# class RegisterView(viewsets.ModelViewSet):# create rest_framework views
#     queryset = EmplyeeRegistration.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = [permissions.IsAuthenticated]

class EmployeeProfileView(generics.GenericAPIView):

    serializer_class=serializers.EmployeeProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all Employee's Profile")
    def get(self,request):
        profiles=EmployeeProfile.objects.all()

        serializer=self.serializer_class(instance=profiles,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="Create Employee Profile")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   




   
# class EmployeeSkillsView(generics.GenericAPIView):

#     serializer_class = serializers.EmployeeSkillSerializer
#     permission_classes = [IsAuthenticated]


#     @swagger_auto_schema(operation_summary="View the detail of an order by its ID")
#     def get(self, request,order_id):


#         order=get_object_or_404(Order,pk=order_id)

        
#         serializer=self.serializer_class(instance=order)

#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     @swagger_auto_schema(operation_summary="Update an order by its ID")
#     def put(self,request,order_id):
        
#         order=get_object_or_404(Order,pk=order_id)
        
#         serializer=self.serializer_class(instance=order,data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(data=serializer.data,status=status.HTTP_200_OK)

#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     @swagger_auto_schema(operation_summary="Delete an order by its ID")
#     def delete(self, request,order_id):
        
#         order =get_object_or_404(Order,id=order_id)

#         order.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
        



