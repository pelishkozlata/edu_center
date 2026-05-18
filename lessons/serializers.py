from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate(self, data):
        lesson_type = data.get('type')
        student = data.get('student')
        group = data.get('group')
        teacher = data.get('teacher')
        start_datetime = data.get('start_datetime')
        end_datetime = data.get('end_datetime')

        if lesson_type == 'INDIVIDUAL':
            if not student:
                raise serializers.ValidationError("Individual lesson must have a student.")
            if group:
                raise serializers.ValidationError("Individual lesson cannot have a group.")

        if lesson_type == 'GROUP':
            if not group:
                raise serializers.ValidationError("Group lesson must have a group.")
            if student:
                raise serializers.ValidationError("Group lesson cannot have a student.")


        if start_datetime and end_datetime and start_datetime >= end_datetime:
            raise serializers.ValidationError("Start must be before end.")

 
        conflicts = Lesson.objects.filter(
            status='SCHEDULED',
            start_datetime__lt=end_datetime,
            end_datetime__gt=start_datetime
        )

        if self.instance:
            conflicts = conflicts.exclude(id=self.instance.id)

        # teacher conflict
        if teacher and conflicts.filter(teacher_id=teacher.id).exists():
            raise serializers.ValidationError("Teacher already has a lesson at this time.")

        # student conflict
        if student and conflicts.filter(student_id=student.id).exists():
            raise serializers.ValidationError("Student already has a lesson at this time.")

        # group conflict
        if group:
            student_ids = group.group_students.filter(
                leave_date__isnull=True
            ).values_list("student_id", flat=True)

            if conflicts.filter(student_id__in=student_ids).exists():
                raise serializers.ValidationError(
                    "One of the group students already has a lesson at this time."
                )

        return data