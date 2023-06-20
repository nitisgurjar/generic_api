from django.urls import path
from .api import StudentApi,StudentCreateApi,RegistrationApi,LoginApi,StudentUpdateApi,StudentDeleteApi,StudentGetApi

urlpatterns = [
    path('',StudentApi.as_view()),
    path('create',StudentCreateApi.as_view()),
    path('register',RegistrationApi.as_view()),
    path('login',LoginApi.as_view()),
    path('update/<int:pk>',StudentUpdateApi.as_view()),
    path('delete/<int:pk>',StudentDeleteApi.as_view()),
    path('get/<int:pk>',StudentGetApi.as_view()),

]
