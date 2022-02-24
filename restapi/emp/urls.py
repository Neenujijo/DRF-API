from .views import LoginAPIView, RegisterView,EmployeeListView,LogoutAPIView,EmployeeDetailsView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
    path('employees/',EmployeeListView.as_view(), name="employees"),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('employee_details/<int:pk>/',EmployeeDetailsView.as_view(),name='employee_details'),
      
]

