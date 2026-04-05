from django.contrib import admin

# Register your models here.

from .models import Branch
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'status')