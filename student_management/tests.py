from django.test import TestCase
from .models import Course, Enrollment, AttendanceRecord
from user_management.models import Student
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(code="CS101", title="Introduction to Computer Science", credit_hours=3)

    def test_course_creation(self):
        course = Course.objects.get(code="CS101")
        self.assertEqual(course.title, "Introduction to Computer Science")

# Additional tests for enrollments and attendance would be similar
class TestCourseSearch(TestCase):
    def setUp(self):
        self.client = APIClient()
        Course.objects.create(code="CS101", title="Intro to CS", credit_hours=3)
        Course.objects.create(code="CS102", title="Advanced CS", credit_hours=4)

    def test_search_course_title(self):
        response = self.client.get('/courses/', {'search': 'Intro'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Intro to CS')
