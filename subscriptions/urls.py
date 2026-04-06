from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path('create/', views.subscription_create, name='subscription_create'),
]