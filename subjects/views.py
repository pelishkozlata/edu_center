from rest_framework import viewsets, permissions
from .models import Subject
from .serializers import SubjectSerializer # Має збігатися з назвою вище
from users.permissions import IsAdminRole

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminRole]