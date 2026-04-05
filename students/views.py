
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            dob=request.POST.get('dob'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            parent_name=request.POST.get('parent_name'),
            parent_phone=request.POST.get('parent_phone'),
            parent_email=request.POST.get('parent_email'),
            parent_relationship=request.POST.get('parent_relationship'),
            branch_id=request.POST.get('branch'),
            is_active=True if request.POST.get('is_active') == 'on' else False,
        )
        return redirect('student_list')

    from branches.models import Branch
    branches = Branch.objects.all()
    return render(request, 'students/student_form.html', {'branches': branches})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.dob = request.POST.get('dob')
        student.phone = request.POST.get('phone')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.parent_name = request.POST.get('parent_name')
        student.parent_phone = request.POST.get('parent_phone')
        student.parent_email = request.POST.get('parent_email')
        student.branch_id = request.POST.get('branch')
        student.is_active = True if request.POST.get('is_active') == 'on' else False
        student.save()
        return redirect('student_detail', pk=student.pk)

    from branches.models import Branch
    branches = Branch.objects.all()
    return render(
        request,
        'students/student_form.html',
        {
            'student': student,
            'branches': branches,
        }
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})