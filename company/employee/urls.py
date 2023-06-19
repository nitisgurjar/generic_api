from django.urls import path
from .api import EmployeeApi,EmployeeCreateApi,EmployeeUpdateApi,EmployeeGetApi,EmployeeDeleteApi

urlpatterns = [
    path('api/create',EmployeeCreateApi.as_view()),
    path('',EmployeeApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/delete/<int:pk>', EmployeeDeleteApi.as_view()),
    path('api/get/<int:pk>',EmployeeGetApi.as_view())
]
