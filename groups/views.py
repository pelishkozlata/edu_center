from rest_framework import viewsets
from .models import Group, GroupStudent
from .serializers import GroupSerializer, GroupStudentSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filterset_fields = ['branch', 'status']
    search_fields = ['name']
    ordering_fields = ['name', 'status', 'id']

class GroupStudentViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer
    filterset_fields = ['group', 'student']
    ordering_fields = ['join_date', 'leave_date', 'id']