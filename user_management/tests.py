from django.test import TestCase
from django.contrib.auth.models import User
from .models import Faculty, Student, Department
from .utils import create_user
from datetime import date

class UserManagementTests(TestCase):
    def test_faculty_creation(self):
        user = create_user('facultyuser', date(1980, 5, 15), 'faculty', faculty_usn='00GA00AD001', position='Professor', password='testpass')
        self.assertEqual(user.user.username, 'facultyuser')
        self.assertTrue(user.is_department_admin, False)

    def test_student_creation(self):
        user = create_user('studentuser', date(2000, 12, 1), 'student')
        self.assertEqual(user.user.username, 'studentuser')
        self.assertEqual(user.usn, '1GA20AD044')
