from .views import LoginAPIView, RegisterView,EmployeeListView,LogoutAPIView
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
    path('employees/',EmployeeListView.as_view(), name="employees"),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
      
]

