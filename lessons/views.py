# lessons/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson
from .forms import LessonForm

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/list.html', {'lessons': lessons})

def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'lessons/form.html', {'form': form})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/detail.html', {'lesson': lesson})