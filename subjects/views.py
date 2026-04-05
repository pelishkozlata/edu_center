from django.shortcuts import render

# Create your views here.
from .models import Subject


def subject_list(request):
    subjects = Subject.objects.select_related('branch').all()

    return render(
        request,
        'subjects/subject_list.html',
        {'subjects': subjects}
    )