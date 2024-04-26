from rest_framework import viewsets
from .models import Course, Enrollment, AttendanceRecord
from .serializers import CourseSerializer, EnrollmentSerializer, AttendanceRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.profile.is_department_admin


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['credits']
    search_fields = ['title']

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semester', 'year', 'course__code']
    
    @action(detail=True, methods=['post'])
    def record_attendance(self, request, pk=None):
        enrollment = self.get_object()
        attendance_data = request.data
        # Assume attendance_data is a list of dates and statuses
        for record in attendance_data:
            AttendanceRecord.objects.create(
                enrollment=enrollment,
                date=record['date'],
                status=record['status']
            )
        return Response({'status': 'attendance recorded'})

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
