from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'groups/form.html', {'form': form})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'group': group})