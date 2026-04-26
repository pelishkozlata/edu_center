from rest_framework import viewsets
from .models import Lesson, LessonTemplate
from .serializers import LessonSerializer, LessonTemplateSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_datetime', 'end_datetime', 'id']


class LessonTemplateViewSet(viewsets.ModelViewSet):
    queryset = LessonTemplate.objects.all()
    serializer_class = LessonTemplateSerializer

    filterset_fields = ['teacher', 'subject', 'group', 'student', 'status', 'type']
    ordering_fields = ['start_date', 'end_date', 'id']