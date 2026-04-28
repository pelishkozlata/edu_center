from rest_framework import viewsets
from .models import Branch
from .serializers import BranchSerializer
from users.permissions import IsAdminRole


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminRole]