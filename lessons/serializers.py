from rest_framework import serializers
from datetime import timedelta
from datetime import datetime
from .models import Lesson, LessonTemplate

def has_lesson_conflict(teacher, student, group, start_datetime, end_datetime, lesson_id=None):
    lessons = Lesson.objects.filter(
        status='SCHEDULED',
        start_datetime__lt=end_datetime,  # урок починається до кінця нового
        end_datetime__gt=start_datetime   # урок закінчується після початку нового
    )

    if lesson_id:
        lessons = lessons.exclude(id=lesson_id)

    if lessons.filter(teacher=teacher).exists():
        return "Teacher has another lesson at this time."

    if student:
        if lessons.filter(student=student).exists():
            return "Student has another lesson at this time."

    if group:
        group_students = group.group_students.filter(leave_date__isnull=True) # ще не вийшли з групи

        for group_student in group_students:
            if lessons.filter(student=group_student.student).exists():
                return f"Student {group_student.student} has another lesson at this time."

    return None

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
    

class LessonTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTemplate
        fields = '__all__'

    def validate(self, data):
        lesson_type = data.get('type')
        student = data.get('student')
        group = data.get('group')
        weekdays = data.get('weekdays')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if lesson_type == 'INDIVIDUAL':
            if not student:
                raise serializers.ValidationError(
                    "Individual lesson template must have a student."
                )
            if group:
                raise serializers.ValidationError(
                    "Individual lesson template cannot have a group."
                )

        if lesson_type == 'GROUP':
            if not group:
                raise serializers.ValidationError(
                    "Group lesson template must have a group."
                )
            if student:
                raise serializers.ValidationError(
                    "Group lesson template cannot have a student."
                )

        if not weekdays:
            raise serializers.ValidationError(
                "Lesson template must have at least one weekday."
            )

        if not isinstance(weekdays, list):
            raise serializers.ValidationError(
                "Weekdays must be a list."
            )
        
        for day in weekdays:
            if day < 0 or day > 6:
                raise serializers.ValidationError(
                    "Each weekday must be between 0 and 6."
                )

        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError(
                "Start time must be before end time."
            )

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError(
                "Start date must be before or equal to end date."
            )

        return data
    
    def create(self, validated_data):
        template = LessonTemplate.objects.create(**validated_data)

        current_date = template.start_date

        while current_date <= template.end_date:
            if current_date.weekday() in template.weekdays:
                start_datetime = datetime.combine(
                    current_date,
                    template.start_time
                )

                end_datetime = datetime.combine(
                    current_date,
                    template.end_time
                )

                conflict = has_lesson_conflict(
                    teacher=template.teacher,
                    student=template.student,
                    group=template.group,
                    start_datetime=start_datetime,
                    end_datetime=end_datetime
                )

                if not conflict:
                    Lesson.objects.create(
                        type=template.type,
                        student=template.student,
                        group=template.group,
                        teacher=template.teacher,
                        subject=template.subject,
                        start_datetime=start_datetime,
                        end_datetime=end_datetime,
                        status='SCHEDULED'
                    )

            current_date += timedelta(days=1)

        return template