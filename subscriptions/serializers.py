from rest_framework import serializers
from .models import StudentSubscription, SubscriptionPlan, PricingTier


class PricingTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingTier
        fields = '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    pricing_tiers = PricingTierSerializer(many=True, read_only=True) # додає до plan всі його pricing tiers у відповіді API

    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class StudentSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubscription
        fields = '__all__'

    def validate(self, data):
        subscription_plan = data.get('subscription_plan')
        subject = data.get('subject')

        if subscription_plan and subject:
            if subject not in subscription_plan.subjects.all():
                raise serializers.ValidationError(
                    "This subject is not included in the selected subscription plan."
                )

            if not subscription_plan.is_active:
                raise serializers.ValidationError(
                    "Cannot assign an inactive subscription plan."
    )

        return data