from rest_framework import serializers
from . models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class LoginSerializers(serializers.Serializer):
    student_email=serializers.EmailField()
    password=serializers.CharField()