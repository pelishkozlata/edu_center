from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            'type',
            'student',
            'group',
            'teacher',
            'subject',
            'start_datetime',
            'end_datetime',
            'status',
        ]