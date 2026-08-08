from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.complex_view),
    re_path('lrt/(?P<toggle>[\d])?', views.long_running_task),
    path('template-cache', views.template_cache)
]

