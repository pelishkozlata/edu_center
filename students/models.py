from django.db import models
from branches.models import Branch


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)

    parent_name = models.CharField(max_length=100, blank=True)
    parent_phone = models.CharField(max_length=20, blank=True)
    parent_email = models.EmailField(blank=True, null=True)
    parent_relationship = models.CharField(max_length=50, blank=True)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='students'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"