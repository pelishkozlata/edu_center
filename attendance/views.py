from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from users.permissions import IsAdminRole
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class AttendanceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.role == 'TEACHER':
            return Attendance.objects.filter(lesson__teacher=user) # attendance.lesson.teacher
        return Attendance.objects.all()

    def get_permissions(self):
        user = self.request.user
        if user.role == 'TEACHER':
            return [IsAuthenticated()] # дозволено доступ, якщо він просто залогінений
        return [IsAdminRole()]
    
    def perform_create(self, serializer):
        lesson = serializer.validated_data['lesson'] # урок, для якого створюють attendance
        if self.request.user.role == 'TEACHER' and lesson.teacher != self.request.user:
            raise PermissionDenied("Not your lesson")
        serializer.save()

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    filterset_fields = ['lesson', 'student', 'status']
    ordering_fields = ['id']