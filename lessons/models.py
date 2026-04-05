from django.db import models
from students.models import Student
from groups.models import Group
from subjects.models import Subject
from users.models import User


class Lesson(models.Model):
    TYPE_CHOICES = [
        ('INDIVIDUAL', 'Individual'),
        ('GROUP', 'Group'),
    ]

    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)

    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='SCHEDULED')

    students = models.ManyToManyField(
        Student,
        through='LessonStudent',
        related_name='lessons'
    )

    def __str__(self):
        return f"{self.subject} {self.start_datetime}"


class LessonStudent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.student} in lesson {self.lesson.id}"