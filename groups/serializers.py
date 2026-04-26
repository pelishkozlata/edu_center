from rest_framework import serializers
from .models import Group, GroupStudent

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = '__all__'

    def validate(self, data):
        group = data.get('group')
        student = data.get('student')

        if group and student and group.branch != student.branch:
            raise serializers.ValidationError(
                "Student must belong to the same branch as the group."
            )
        return data