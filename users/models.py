from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone number is required")
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault('role', 'admin') 

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
  
    phone = models.CharField(max_length=20, unique=True, verbose_name="Телефон")
    

    first_name = models.CharField(max_length=150, blank=True, verbose_name="Ім'я")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Прізвище")
    
  
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student', verbose_name="Роль")


    branch = models.ForeignKey(
        'branches.Branch', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='users',
        verbose_name="Філіал"
    )


    is_active = models.BooleanField(default=True, verbose_name="Активний")
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Дата реєстрації")

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []  

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.phone} ({self.first_name} {self.last_name})".strip()