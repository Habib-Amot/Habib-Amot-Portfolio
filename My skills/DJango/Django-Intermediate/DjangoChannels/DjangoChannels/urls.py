from django.contrib import admin
from django.urls import path, include
from channels.routing import ProtocolTypeRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls'))
]
