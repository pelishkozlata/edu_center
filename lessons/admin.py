from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'teacher', 'subject', 'start_datetime', 'end_datetime', 'status')
    list_filter = ('type', 'status', 'teacher', 'subject')
    search_fields = ('teacher__username', 'subject__name')
