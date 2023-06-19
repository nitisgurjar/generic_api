from django.db import models

class Employee(models.Model):
    emp_regno=models.TextField(unique=True)
    emp_name=models.TextField()
    emp_email=models.TextField()
    emp_mobile=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now=True)
