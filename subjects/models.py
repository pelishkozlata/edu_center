from django.db import models

# Create your models here.
from django.db import models
from branches.models import Branch


class Subject(models.Model):
    name = models.CharField(max_length=255)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    status = models.CharField(
        max_length=20,
        default='active'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'branch'],
                name='unique_subject_per_branch'
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.branch.name})"