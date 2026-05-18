from rest_framework import viewsets
from .serializers import SubscriptionPlanSerializer, StudentSubscriptionSerializer, PricingTierSerializer
from .models import SubscriptionPlan, StudentSubscription, PricingTier
from users.permissions import IsAdminRole


class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.select_related(
        "branch"
    ).prefetch_related(
        "subjects"
    )

    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminRole]

    filterset_fields = ['branch', 'type', 'is_active', 'subjects']
    search_fields = ['name']
    ordering_fields = ['name', 'type', 'is_active', 'id']

class PricingTierViewSet(viewsets.ModelViewSet):
    queryset = PricingTier.objects.select_related(
        "subscription_plan"
    )

    serializer_class = PricingTierSerializer
    permission_classes = [IsAdminRole]

    filterset_fields = ['subscription_plan', 'lessons_per_month']
    ordering_fields = ['lessons_per_month', 'price_per_lesson', 'id']

class StudentSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = StudentSubscription.objects.select_related(
        "student",
        "subscription_plan",
        "subject"
    )

    serializer_class = StudentSubscriptionSerializer
    permission_classes = [IsAdminRole]

    filterset_fields = ['student', 'subscription_plan', 'subject', 'status']
    ordering_fields = ['start_date', 'id']