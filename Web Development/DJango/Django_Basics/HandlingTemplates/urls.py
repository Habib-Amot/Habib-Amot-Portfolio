from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_template, name="template-view")
]
