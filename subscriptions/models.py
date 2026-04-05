from django.db import models
from branches.models import Branch
from subjects.models import Subject


class SubscriptionPlan(models.Model):
    TYPE_CHOICES = [
        ('INDIVIDUAL', 'Individual'),
        ('GROUP', 'Group'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ARCHIVED', 'Archived'),
    ]

    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    subjects = models.ManyToManyField(Subject)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.name


class PricingTier(models.Model):
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE,
        related_name='pricing_tiers'
    )

    lessons_per_month = models.PositiveIntegerField()
    price_per_lesson = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.lessons_per_month} → {self.price_per_lesson}"