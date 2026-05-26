from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from branches.models import Branch
from users.models import User
from students.models import Student
from subjects.models import Subject
from .models import Lesson

class LessonSimpleSuccessTest(TestCase):
    def test_create_lesson_successfully(self):
        branch = Branch.objects.create(name="Львів", city="Львів", status="active")
        teacher = User.objects.create_user(phone="+380990000066", password="password123", role="TEACHER")
        student = Student.objects.create(first_name="Олег", last_name="Тест", branch=branch)
        subject = Subject.objects.create(name="Програмування", branch=branch)

       
        tz = timezone.get_current_timezone()
        start = datetime(2026, 5, 25, 10, 0).replace(tzinfo=tz)
        end = datetime(2026, 5, 25, 11, 0).replace(tzinfo=tz)

       
        lesson = Lesson.objects.create(
            type="INDIVIDUAL",
            teacher=teacher,
            student=student,
            subject=subject,
            start_datetime=start,
            end_datetime=end,
            status="SCHEDULED"
        )

        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(lesson.status, "SCHEDULED")