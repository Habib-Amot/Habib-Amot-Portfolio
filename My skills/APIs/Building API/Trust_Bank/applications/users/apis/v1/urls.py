from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.LoginView.as_view(), name='user-login'),
    path('auth/register', views.RegistrationView.as_view(), name='user-register'),
    path('dashboard', views.UserDashboardView.as_view(), name='user-dashboard')
]
