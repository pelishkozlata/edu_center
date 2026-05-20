from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsAdminRole
from .models import Lesson, LessonTemplate
from .serializers import LessonSerializer, LessonTemplateSerializer


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        user = self.request.user

        qs = Lesson.objects.select_related(
            "teacher",
            "subject",
            "student",
            "group"
        )

        if user.is_authenticated and getattr(user, 'role', None) == 'teacher':
            qs = qs.filter(teacher=user)

        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminRole()]

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_datetime', 'end_datetime', 'id']

class LessonTemplateViewSet(viewsets.ModelViewSet):
    queryset = LessonTemplate.objects.select_related(
        "teacher",
        "subject",
        "student",
        "group"
    )
    serializer_class = LessonTemplateSerializer
    permission_classes = [IsAdminRole]

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_date', 'end_date', 'id']