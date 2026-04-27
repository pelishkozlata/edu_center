from django.shortcuts import render

# Create your views here.

from .models import Branch
from django.shortcuts import redirect


def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branches': branches})


def branch_delete(request): 
    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        Branch.objects.filter(id=branch_id).delete()

    return redirect('branch_list')
