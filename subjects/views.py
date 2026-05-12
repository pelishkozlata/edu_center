from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Subject
from .serializers import SubjectSerializer
from users.permissions import IsAdminRole

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminRole]


'''
class SubjectCreateViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SubjectSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    
    def list(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        subject = get_object_or_404(Subject, pk = pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        subject = get_object_or_404(Subject, pk = pk)
        serializer = SubjectSerializer(subject, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status = 400)
    
    def destroy(self, request, pk = None):
        subject = get_object_or_404(Subject, pk = pk)
        subject.delete()
        return Response(status = 204)
'''