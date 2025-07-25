import datetime
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory
from .forms import NameForm, ArticleForm, BookForm
from UsingModels.models import Book, Author, Publisher

# Create your views here.

def basic_form(request, num_of_user=''):
    # to make this form to be able to handle formset logic, whereby we can pass the number of forms that we want to create at a time
    # this makes this view to be able to act as a single form data handler or multiple form data handler
    num_of_user = int(num_of_user) if (num_of_user and int(num_of_user) > 1) else ''
    if not num_of_user:
        if request.method == "GET":
            name_form = NameForm()
            return render(request, 'name.html', context={'form':name_form})
        elif request.method == "POST":
            submitted_form_data = NameForm(request.POST)
            if submitted_form_data.is_valid():
                return HttpResponse("thanks for your kind gesture and time")
            else:
                return render(request, 'name.html', {'form':submitted_form_data})
        return HttpResponse("this is the return of the basic form class")
    else:
        name_formset = formset_factory(NameForm, extra=num_of_user, max_num=4, min_num=3)
        if request.method == "GET":
            # passing initial data to a formset makes the formset to be displayed with the data that is being passed into it
            # the initial data has higher precedence than the max_num of data that can be displayed
            # this means that regradless of the number of max data that can be displayed in the formset, the initial data will always be displyed

            initial_data = [
                {'my_name': 'Prudent Amot', 'about_me': "Prudent Amot is a very strong and flexible backender with some mix in the frontend part", 'passord': "TestPassword"},
                {'my_name': 'Prudent Amot', 'about_me': "Prudent Amot is a very strong and flexible backender with some mix in the frontend part", 'passord': "TestPassword"},
                {'my_name': 'Prudent Amot', 'about_me': "Prudent Amot is a very strong and flexible backender with some mix in the frontend part", 'passord': "TestPassword"},
            ]
            return render(request, 'name_formset.html', context={'formset':name_formset(initial=initial_data), 'num_of_user':num_of_user, 'form_url': 'basic-form'})
        else:
            submitted_form_data = name_formset(request.POST)
            if submitted_form_data.is_valid():
                return HttpResponse("thanks for entering multiple data into the form")
            else:
                return HttpResponse(submitted_form_data.errors)

# this view is responsible for handling complex formset data
# in the sense that the data is being passed is verified before any further action is being taken on the form
def complex_form(request, extra_value=''):
    # creating a formset from the ArticleForm class
    extra_value = int(extra_value) if (extra_value and int(extra_value) > 1) else ''

    ArticleForm_Factory = formset_factory(ArticleForm, extra=extra_value if extra_value else 1, max_num=4, can_delete=True)
    initial = [
        {'title': "the man with the big snake", 'pub_date': datetime.date.today()},
        {'title': "the man with the big snake", 'pub_date': datetime.date.today()},
        {'title': "the man with the big snake", 'pub_date': datetime.date.today()},
    ]
    if request.method == "GET":
        # assuming we want to pass some initial data to the form
        ArticleForm_Factory = ArticleForm_Factory(initial=initial)
        return render(request, 'complex-form.html', context={'article_formset': ArticleForm_Factory, 'form_url': 'complex-form', 'extra_value': extra_value})
    elif request.method == "POST":
        submitted_data = ArticleForm_Factory(request.POST)
        if submitted_data.is_valid():
            for form in submitted_data:
                print(form.cleaned_data)
            return HttpResponse("thanks for the submitted data")
        else:
            return HttpResponse('the data that you submitted is invalid')


# this view handles form data that is being used to change or modify model data of and object
# in other words, this view will modify a record that is being saved in the database 
# for example, this view is used to modify books that is being saved in the database
def  edit_book(request, book_index):
    if request.method == "GET":
        book = get_object_or_404(Book, id=book_index)
        book_form = BookForm(instance=book)
        return render(request, 'ModelForm.html', {'form': book_form, 'book_index':book_index})
    
    if request.method == "POST":
        book = get_object_or_404(Book, id=book_index)
        submitted_data = BookForm(request.POST, instance=book)
        if submitted_data.is_valid():
            if submitted_data.has_changed():
                submitted_data.save()
                return HttpResponse("Data edited successfully")
            else:
                messages.info(request, "no data changed or altered")
                return redirect(book.get_absolute_url())
        else:
            messages.error(request, "invalid book entries")
            return redirect(book.get_absolute_url())

# this view is being controlled by making use of database transaction to make sure that all data is being writtten or not written at all
# removing the atomicity will only make part of the changes to be written into the database while some part will fail
# this is the exact thing that we dont want to happen with user data
@transaction.atomic
def edit_mutliple_books(request, author_id):
    # this is just a basic form that includes not validtion of objects and checks for authentication or authorizations whatsoever
    # this view is just to show how to handle multiple data that is being submitted in the modelformset 
    author = Author.objects.get(id=author_id)
    publisher = Publisher.objects.get(name__iexact="DEFAULT")
    author_books = Book.objects.prefetch_related('authors').filter(authors__id=author_id).order_by('-pub_date')[:3]
    date = datetime.date.today()
    BookFactory = modelformset_factory(Book, fields=('title', 'price'), extra=1)

    if request.method == "GET":
        return render(request, 'mutilple-books-edit.html', {'form': BookFactory(queryset=author_books), 'author_id':author_id})
    else:
        submitted_data = BookFactory(request.POST, queryset=author_books)
        if submitted_data.is_valid():
            instances = submitted_data.save(commit=False)
            for instance in instances:
                if instance.pk is not None:
                    instance.save()
                else:
                    instance.pub_date = date
                    instance.publisher = publisher
                    instance.save()
            return HttpResponse('thanks for submitting the data')
        else:
            return HttpResponse('the submitted data is invalid')

