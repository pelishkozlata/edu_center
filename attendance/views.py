from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from users.permissions import IsAdminRole
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user = self.request.user

        qs = Attendance.objects.select_related(
            "lesson",
            "student"
        )

        if user.is_authenticated and getattr(user, 'role', None) == 'teacher':
            return qs.filter(lesson__teacher=user)

        return qs

    def get_permissions(self):
        if self.request.user.is_authenticated and getattr(self.request.user, 'role', None) == 'teacher':
            return [IsAuthenticated()]
        return [IsAdminRole()]

    def perform_create(self, serializer):
        lesson = serializer.validated_data['lesson']

        if lesson.status == "CANCELLED":
            raise PermissionDenied("Lesson is cancelled")

        if self.request.user.role == 'TEACHER' and lesson.teacher != self.request.user:
            raise PermissionDenied("Not your lesson")

        serializer.save()