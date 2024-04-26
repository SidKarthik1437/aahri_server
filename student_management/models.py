from django.db import models
from user_management.models import Student

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    year = models.IntegerField()

    class Meta:
        unique_together = ('student', 'course', 'semester', 'year')

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.code} for {self.semester} {self.year}"

class AttendanceRecord(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('excused', 'Excused')])

    def __str__(self):
        return f"{self.enrollment.student.name} - {self.status} on {self.date}"
