# attendance/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance
from .forms import AttendanceForm

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/list.html', {'records': records})

def attendance_mark(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/form.html', {'form': form})