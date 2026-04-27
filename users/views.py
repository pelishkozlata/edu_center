from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer # Переконайся, що створила цей серіалайзер

User = get_user_model()

# Це те, що шукає твій urls.py
class LoginView(TokenObtainPairView):
    # Кастомний серіалізатор, щоб додати роль у відповідь (вимога ТЗ)
    class CustomTokenSerializer(TokenObtainPairSerializer):
        def validate(self, attrs):
            data = super().validate(attrs)
            # Система повертає роль, ім'я та доступні філіали
            data['role'] = self.user.role if hasattr(self.user, 'role') else 'ADMIN'
            data['full_name'] = f"{self.user.first_name} {self.user.last_name}"
            return data
    
    serializer_class = CustomTokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Тільки адмін може керувати акаунтами вчителів
    permission_classes = [permissions.IsAdminUser]