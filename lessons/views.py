from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsAdminRole
from .models import Lesson, LessonTemplate
from .serializers import LessonSerializer, LessonTemplateSerializer


class LessonViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.role == 'TEACHER':
            return Lesson.objects.filter(teacher=user)
        return Lesson.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminRole()]

    serializer_class = LessonSerializer

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_datetime', 'end_datetime', 'id']


class LessonTemplateViewSet(viewsets.ModelViewSet):
    queryset = LessonTemplate.objects.all()
    serializer_class = LessonTemplateSerializer
    permission_classes = [IsAdminRole]

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_date', 'end_date', 'id']
