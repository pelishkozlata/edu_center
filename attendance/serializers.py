from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):
        lesson = data.get('lesson')
        student = data.get('student')

        if not lesson:
            raise serializers.ValidationError(
                "Attendance must be linked to a lesson."
            )
        if not student:
            raise serializers.ValidationError(
                "Attendance must have a student."
            )
        
        # чи цей студент той, який привʼязаний до уроку
        if lesson.type == "INDIVIDUAL":
            if lesson.student != student:
                raise serializers.ValidationError(
                    "This student is not assigned to the individual lesson."
                )
            
        if lesson.type == "GROUP":
            if not lesson.group:
                raise serializers.ValidationError(
                    "Group lesson must have a group."
                )
            
        # перевірка що студент в групі
            if not lesson.group.group_students.filter(student=student).exists():
                raise serializers.ValidationError(
                    "This student is not in the group for this lesson."
                )

        return data