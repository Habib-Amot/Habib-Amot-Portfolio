from django.urls import path, re_path, include
from . import views

# handling the urls for the views
# this is the urls.py file that handles the urls for the views
# it is used to map the urls to the views
extended_patterns = [
    path('',  views.year_archive, name="http-year_archive"),
    re_path("(?P<month>[\d]{1,2})/?$", views.month_archive, name="http-year_archive"),
    re_path("(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/?$", views.day_archive, name="http-year_archive")

]
urlpatterns = [
    path('', views.home, name="http-homepage"),
    re_path("^articles/(\d{4})/", include(extended_patterns)),
    re_path("^articles/(?P<year>\d{4})/", include(extended_patterns)),
    re_path("^articles/(?P<year>\d{4})/", include(extended_patterns)),
    path('register', views.register, name="http-register"),
    path('admin_register', views.admin_register, name="admin-register"),
    path('name-data', views.name_form_view, name='name-form-view'),
    path('create-author', views.create_author, name='author-creation-view'),
    path('create-book', views.create_book, name='book-creation-view')
]

