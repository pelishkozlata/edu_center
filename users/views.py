from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer 

User = get_user_model()


class LoginView(TokenObtainPairView):

    class CustomTokenSerializer(TokenObtainPairSerializer):
        def validate(self, attrs):
            data = super().validate(attrs)
            data['role'] = self.user.role if hasattr(self.user, 'role') else 'ADMIN'
            data['full_name'] = f"{self.user.first_name} {self.user.last_name}"
            return data
    
    serializer_class = CustomTokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]