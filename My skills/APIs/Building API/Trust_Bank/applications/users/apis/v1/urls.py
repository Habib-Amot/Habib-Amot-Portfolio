from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='user-login'),
    path('auth/refresh', TokenRefreshView.as_view(), name='refresh-token'),
    path('dashboard', views.UserDashboardView.as_view(), name='user-dashboard'),
    path('auth/register', views.RegistrationView.as_view(), name='user-register'),
    path('transactions', views.AllUserTransactions.as_view(), name='user-transactions')
]
