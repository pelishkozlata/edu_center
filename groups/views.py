from rest_framework import viewsets
from .models import Group, GroupStudent
from .serializers import GroupSerializer, GroupStudentSerializer
from users.permissions import IsAdminRole


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.select_related(
        "branch"
    ).prefetch_related(
        "group_students__student"
    )

    serializer_class = GroupSerializer
    filterset_fields = ['branch', 'status']
    search_fields = ['name']
    ordering_fields = ['name', 'status', 'id']
    permission_classes = [IsAdminRole]

class GroupStudentViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.select_related(
        "group",
        "student"
    )

    serializer_class = GroupStudentSerializer
    filterset_fields = ['group', 'student']
    ordering_fields = ['join_date', 'leave_date', 'id']
    permission_classes = [IsAdminRole]