from rest_framework import serializers
from .models import Lesson, LessonTemplate


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate(self, data):
        lesson_type = data.get('type')
        student = data.get('student')
        group = data.get('group')
        start_datetime = data.get('start_datetime')
        end_datetime = data.get('end_datetime')

        if lesson_type == 'INDIVIDUAL':
            if not student:
                raise serializers.ValidationError(
                    "Individual lesson must have a student."
                )
            if group:
                raise serializers.ValidationError(
                    "Individual lesson cannot have a group."
                )

        if lesson_type == 'GROUP':
            if not group:
                raise serializers.ValidationError(
                    "Group lesson must have a group."
                )
            if student:
                raise serializers.ValidationError(
                    "Group lesson cannot have a student."
                )

        if start_datetime and end_datetime and start_datetime >= end_datetime:
            raise serializers.ValidationError(
                "Start datetime must be before end datetime."
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

        if not isinstance(weekdays, list): # перевіряємо чи weekdays це список
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