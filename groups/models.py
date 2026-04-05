from django.db import models
from students.models import Student
from branches.models import Branch


class Group(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ARCHIVED', 'Archived'),
    ]

    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.name


class GroupStudent(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True
    )

    join_date = models.DateField(auto_now_add=True)
    leave_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} in {self.group}"