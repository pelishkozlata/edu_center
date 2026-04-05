from django.contrib import admin

# Register your models here.
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'branch',
        'is_active',
    )
    list_filter = ('branch', 'is_active')
    search_fields = ('first_name', 'last_name', 'phone', 'email')