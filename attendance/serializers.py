from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):
        lesson = data.get('lesson')
        student = data.get('student')

        if not lesson or not student:
            raise serializers.ValidationError("Lesson and student are required.")

        if Attendance.objects.filter(lesson=lesson, student=student).exists():
            raise serializers.ValidationError("Attendance already exists.")

        if lesson.type == "INDIVIDUAL":
            if lesson.student != student:
                raise serializers.ValidationError(
                    "Student not assigned to this lesson."
                )

        if lesson.type == "GROUP":
            if not lesson.group:
                raise serializers.ValidationError(
                    "Group lesson must have a group."
                )

            if not lesson.group.group_students.filter(student_id=student.id).exists():
                raise serializers.ValidationError(
                    "Student not in group."
                )

        return data