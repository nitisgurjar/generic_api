from django.http import QueryDict
from rest_framework import generics
from rest_framework.response import Response
from . serializers import StudentSerializers,LoginSerializers
from . models import Student
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class StudentApi(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentCreateApi(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentGetApi(generics.RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentDeleteApi(generics.DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentUpdateApi(generics.UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class RegistrationApi(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def post(self,request):
        data=request.POST.copy()
        password=data.get('password')
        data['password']=make_password(password)

        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        Student=serializer.save()
        refresh=RefreshToken.for_user(Student)
        token={
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        }
        return Response(token)
    
class LoginApi(generics.CreateAPIView):
    serializer_class=LoginSerializers

    def post(self,request):
        serializers=self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        student_email=serializers.validated_data['student_email']
        password=serializers.validated_data['password']

        try:
            student=Student.objects.get(student_email=student_email)
        except Student.DoesNotExist:
            return Response({'error':'invalid email'},status=400)
        if not check_password(password,student.password):
            return Response({'error':'invalid password'},status=400)
        refresh=RefreshToken.for_user(student)
        response_data={
            'email':student_email,
            'access_token':str(refresh.access_token)
        }

        return Response(response_data)