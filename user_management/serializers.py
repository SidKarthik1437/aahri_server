from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Faculty, Student, Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name' ]

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ['user', 'usn', 'date_of_birth', 'department', 'semester']

class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Faculty
        fields = ['user', 'faculty_usn', 'position', 'is_department_admin', 'is_system_admin', 'department']
