# user_management/models.py

from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

class Student(Profile):
    usn = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    semester = models.IntegerField(null=True, blank=True)
    # Additional student-specific fields
    
    def __str__(self):
        return f"{self.usn} - {self.department.name if self.department else 'No Department'}"


class Faculty(Profile):
    faculty_usn = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=100)
    is_department_admin = models.BooleanField(default=False)
    is_system_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usn} - {self.employee_usn} ({'Admin' if self.is_department_admin else 'Faculty'})"
