from django.db import models

class Student(models.Model):
    student_regno=models.TextField(unique=True)
    student_name=models.TextField()
    student_email=models.TextField()
    student_mobile=models.TextField(null=True)
    password=models.CharField(max_length=260)
    created_at=models.DateTimeField(auto_now=True)
