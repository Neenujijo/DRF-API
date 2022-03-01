from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('register', views.RegisterView)
router.register('profile', views.EmployeeProfileView)
router.register('skills', views.EmployeeSkillsView)

urlpatterns = [
    path('', include(router.urls))
]

