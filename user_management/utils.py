from django.contrib.auth.models import User
from .models import Faculty, Student
from datetime import date

def create_user(username, date_of_birth, user_type, **extra_fields):
    password = date_of_birth.strftime('%Y%m%d') if user_type == 'student' else extra_fields.get('password', 'defaultpass')
    user = User.objects.create_user(
        username=username,
        password=password,
        **extra_fields
    )
    profile_class = Student if user_type == 'student' else Faculty
    return profile_class.objects.create(user=user, date_of_birth=date_of_birth, **extra_fields)
