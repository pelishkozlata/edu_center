from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer 

class StudentViewSet(viewsets.ModelViewSet):
    """
    Цей клас автоматично замінює всі функції: 
    list, create, retrieve, update, destroy.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer