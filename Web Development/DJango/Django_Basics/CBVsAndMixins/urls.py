from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='cbv-view'),
    path('author/', views.AuthorView.as_view(), name='author-cbv'),
    path('author/<int:pk>', views.AuthorDetails.as_view(), name='author-details'),
    path('author/login', views.AuthorLogin.as_view(), name='author-login'),
    path('author/create', views.AuthorCreate.as_view(), name='author-create'),
    path('author/mx/<int:pk>', views.AuthorMixin.as_view(), name='author-mx'),
    path('author/singleMx/<int:pk>', views.SingleAuthorBooks.as_view(), name='single-author-book-view'),
    path('author/ax/<int:pk>', views.AuthorAjaxResponse.as_view(), name='author-ajax-response')
]

