from django.urls import path
from . import views 
from HandlingHttpRequest.views import vote

urlpatterns = [
    path('', views.home.as_view(), name='homepage'),
    path('result/<int:pk>', views.result.as_view(), name='resultpage'),
    path('detail/<int:pk>', views.detail.as_view(), name='detailpage'),
    path('vote/<int:poll_id>', vote, name='votepage')
]
