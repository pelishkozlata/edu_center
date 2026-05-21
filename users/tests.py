from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):

    def test_create_user_with_phone(self):
        user = User.objects.create_user(
            phone="+380991112233",
            password="securepassword123",
            first_name="Sofia",
            role="TEACHER"  
        )
        self.assertEqual(user.phone, "+380991112233")
        self.assertTrue(user.is_active)
        self.assertEqual(user.role, 'TEACHER')

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            phone="+380995556677",
            password="adminpassword"
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)