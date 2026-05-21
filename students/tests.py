from django.test import TestCase

# Create your tests here.
from branches.models import Branch
from students.models import Student

class StudentBasicTest(TestCase):
    def test_create_student_successfully(self):
        branch = Branch.objects.create(name="Львів-Центр", city="Львів", status="active")

        student = Student.objects.create(
            first_name="Софія", 
            last_name="Тест", 
            branch=branch
        )

        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(student.first_name, "Софія")
        self.assertEqual(student.branch.name, "Львів-Центр")