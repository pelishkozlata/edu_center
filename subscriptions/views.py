from rest_framework import viewsets
from .serializers import SubscriptionPlanSerializer, StudentSubscriptionSerializer, PricingTierSerializer
from .models import SubscriptionPlan, StudentSubscription, PricingTier


class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

    filterset_fields = ['branch', 'type', 'is_active', 'subjects']
    search_fields = ['name']
    ordering_fields = ['name', 'type', 'is_active', 'id']


class PricingTierViewSet(viewsets.ModelViewSet):
    queryset = PricingTier.objects.all()
    serializer_class = PricingTierSerializer

    filterset_fields = ['subscription_plan', 'lessons_per_month']
    ordering_fields = ['lessons_per_month', 'price_per_lesson', 'id']


class StudentSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = StudentSubscription.objects.all()
    serializer_class = StudentSubscriptionSerializer

    filterset_fields = ['student', 'subscription_plan', 'subject', 'status']
    ordering_fields = ['start_date', 'id']