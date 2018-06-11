from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    BookFormset,
    BookModelFormset,
    BookModelForm,
    AuthorFormset
)
from .models import Book, Author


def create_book_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            return redirect('store:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class BookListView(generic.ListView):

    model = Book
    context_object_name = 'books'
    template_name = 'store/list.html'


def create_book_model_form(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('store:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


def create_book_with_authors(request):
    template_name = 'store/create_with_author.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = book
                author.save()
            return redirect('store:book_list')
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })
