from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer): # Перевір великі літери S
    class Meta:
        model = Subject
        fields = '__all__'