from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# # router.register('register', views.RegisterView)
# router.register('profile/', views.EmployeeProfileView)
# # router.register('skills', views.EmployeeSkillsView)
# # router.register('login', views.EmployeeLoginView)

urlpatterns = [
   path('profiles/',views.EmployeeProfileView.as_view(),name='orders'),
   

]

