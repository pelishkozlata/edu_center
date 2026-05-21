from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from datetime import datetime
from branches.models import Branch
from users.models import User
from students.models import Student
from subjects.models import Subject
from lessons.models import Lesson
from attendance.models import Attendance 

class AttendanceBasicTest(TestCase):
    def setUp(self):
 
        branch = Branch.objects.create(name="Львів", city="Львів", status="active")
        teacher = User.objects.create_user(phone="+380990000055", password="password123", role="TEACHER")
        self.student = Student.objects.create(first_name="Олена", last_name="Тест", branch=branch)
        subject = Subject.objects.create(name="Англійська", branch=branch)
        
    
        tz = timezone.get_current_timezone()
        self.lesson = Lesson.objects.create(
            type="INDIVIDUAL",
            teacher=teacher,
            student=self.student,
            subject=subject,
            start_datetime=datetime(2026, 5, 20, 10, 0).replace(tzinfo=tz),
            end_datetime=datetime(2026, 5, 20, 11, 0).replace(tzinfo=tz),
            status="COMPLETED"
        )

    def test_create_attendance_successfully(self):
   
        attendance = Attendance.objects.create(
            lesson=self.lesson,
            student=self.student,
            status="PRESENT" 
        )
        
        self.assertEqual(Attendance.objects.count(), 1)
        self.assertEqual(attendance.status, "PRESENT")