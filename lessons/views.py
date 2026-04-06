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
            lesson = form.save(commit=False)

            if lesson.type == 'INDIVIDUAL' and not lesson.student:
                form.add_error('student', 'Required for individual lesson')

            elif lesson.type == 'GROUP' and not lesson.group:
                form.add_error('group', 'Required for group lesson')

            else:
                lesson.save()
                return redirect('lesson_list')

    else:
        form = LessonForm()

    return render(request, 'lessons/form.html', {'form': form})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/detail.html', {'lesson': lesson})