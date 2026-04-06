from django import forms
from .models import SubscriptionPlan


class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = [
            'name',
            'branch',
            'type',
            'subjects',
            'status',
        ]