# subscriptions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SubscriptionPlan
from .forms import SubscriptionPlanForm

def subscription_list(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/list.html', {'plans': plans})

def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionPlanForm()
    return render(request, 'subscriptions/form.html', {'form': form})