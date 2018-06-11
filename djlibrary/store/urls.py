from django.urls import re_path

from .views import (
    create_book_normal,
    create_book_model_form,
    create_book_with_authors,
    BookListView,
)

app_name = 'store'

urlpatterns = [

    re_path(r'^book/create_normal', create_book_normal, name='create_book_normal'),
    re_path(r'^book/create_model', create_book_model_form, name='create_book_model_form'),
    re_path(r'^book/create_with_author', create_book_with_authors, name='create_book_with_authors'),
    re_path(r'^book/list', BookListView.as_view(), name='book_list'),

]
