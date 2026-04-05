from django.shortcuts import render

# Create your views here.

from .models import Branch


def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branches': branches})