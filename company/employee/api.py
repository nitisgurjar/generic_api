from rest_framework import generics
from . models import *
from . serializers import EmployeeSerializers

class EmployeeCreateApi(generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeApi(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeUpdateApi(generics.UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeGetApi(generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers