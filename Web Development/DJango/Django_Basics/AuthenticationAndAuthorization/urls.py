from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user-homepage'),
    path('register', views.Register.as_view(), name='user-registration'),
    path('login', views.user_login, name='user-login'),
    path('logout', views.user_logout, name='user-logout'),
    path('dashboard', views.dashboard, name='user-dashboard'),
    path('view-users', views.all_users, name='all-users-view')
]
