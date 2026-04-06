from django.contrib import admin
from .models import SubscriptionPlan, PricingTier

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'type', 'status') 
    list_filter = ('type', 'status', 'branch')          
    search_fields = ('name', )                          

@admin.register(PricingTier)
class PricingTierAdmin(admin.ModelAdmin):
    list_display = ('subscription_plan', 'lessons_per_month', 'price_per_lesson')
    list_filter = ('subscription_plan', )