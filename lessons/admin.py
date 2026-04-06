from django.contrib import admin
from .models import Lesson, LessonStudent

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'teacher', 'subject', 'start_datetime', 'end_datetime', 'status')
    list_filter = ('type', 'status', 'teacher', 'subject')
    search_fields = ('teacher__username', 'subject__name')


@admin.register(LessonStudent)
class LessonStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'student')
    list_filter = ('lesson',)
    search_fields = ('student__full_name', 'lesson__subject__name')