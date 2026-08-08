from django.urls import include, path

urlpatterns = [
    path('v1/users/', include('applications.users.apis.v1.urls'))
]