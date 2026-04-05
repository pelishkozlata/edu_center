from django.db import models
from lessons.models import Lesson
from students.models import Student


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    note = models.TextField(blank=True)

    class Meta:
        unique_together = ('lesson', 'student')

    def __str__(self):
        return f"{self.student} - {self.status}"