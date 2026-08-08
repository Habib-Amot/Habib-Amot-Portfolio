from django.urls import path,re_path
from . import views 


urlpatterns = [
    re_path('basic/(?P<num_of_user>[0-9]+)?$', views.basic_form, name="basic-form"),
    re_path('complex/(?P<extra_value>[0-9]+)?$', views.complex_form, name="complex-form"),
    path('edit/<int:book_index>', views.edit_book, name='edit-book'),
    path('edit/multiple/<int:author_id>', views.edit_mutliple_books, name="edit-multiple-books")
]
