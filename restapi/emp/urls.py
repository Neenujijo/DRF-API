from .views import LoginAPIView, RegisterView,EmployeeListView
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
    path('employees/',EmployeeListView.as_view(), name="employees"),
    path('login/', LoginAPIView.as_view(), name='login'),
    
    
]

