from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, StudentViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'students', StudentViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
