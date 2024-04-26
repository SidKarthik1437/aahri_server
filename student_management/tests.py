from django.test import TestCase
from .models import Course, Enrollment, AttendanceRecord
from user_management.models import Student
from django.contrib.auth.models import User

class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(code="CS101", title="Introduction to Computer Science", credit_hours=3)

    def test_course_creation(self):
        course = Course.objects.get(code="CS101")
        self.assertEqual(course.title, "Introduction to Computer Science")

# Additional tests for enrollments and attendance would be similar
