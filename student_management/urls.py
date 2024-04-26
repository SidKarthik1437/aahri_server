from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EnrollmentViewSet, AttendanceRecordViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'attendance', AttendanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
