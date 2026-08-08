from django.urls import path, re_path, include

urlpatterns = [
    path('', include('applications.users.urls')),
    re_path('user/', include('applications.users.urls')),
    re_path('panel/', include('applications.users.urls'))
]
