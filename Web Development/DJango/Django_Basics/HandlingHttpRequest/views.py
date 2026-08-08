from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.template.loader import get_template, select_template
from .forms import RegistrationForm, AdminRegister, BasicForm, AuthorForm, BookForm
from PollsApp.models import Question, Choice
from UsingModels.models import Author, Book



# Create your views here.

#  creating views that handle user request from urls 
def home(request):
    return redirect(reverse('admin:login'))

def year_archive(request, year=None):
    if year == None:
        return redirect(reverse('polls:month_archive', args=(2025,)))
    else:
        return HttpResponse(f"this is the view for year archive {year} okk")

def month_archive(request, year=2025, month=1):
    if year == None:
        return redirect(reverse('polls:month_archive', args=(2025,)))
    else:
        return HttpResponse(f"this is the view for year archive {year} okk")

def day_archive(request, year=2025, month=1, day=1):
    return HttpResponse(f"this is the view for year archive {year}, month {month} and day {day}")

# handling of uploaded files using Form fields
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
        # return HttpResponse("Please submit the form to register.")
    elif request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # processing the form data
            with open('uploaded_data'+request.FILES['profile_picture'].name, 'wb+') as destination:
                for chunk in request.FILES['profile_picture'].chunks():
                    destination.write(chunk)
            return HttpResponse("Registration successful!")
        else:
            return HttpResponse("Invalid form data. Please try again.")

# this is just a dummy admin page that can be used to register users with a profile picture
@require_http_methods(["GET", "POST"])
def admin_register(request):
    if request.method == "GET":
        form = AdminRegister()
        return render(request, 'register.html', {'form': form})
    elif request.method == "POST":
        form_fields  = AdminRegister(request.POST, request.FILES)
        if form_fields.is_valid():
            form_fields.save()
            return HttpResponse('Admin registration completed successfully')
        else:
            print(form_fields.errors)
            return HttpResponse("Invalid Form Parameters....please trya again")

# creating a view that allows users to upload more than one file
""" @require_http_methods(["GET", "POST"])
def upload_multiple_files(request):
    if request.method == 'GET':
        pass """

# dealing with user session 
# by making use of the polls app from my django basics project, I want to make sure that only one user can vote at a time
# and also any authenticated user can vote only once
@require_http_methods(["GET", "POST"])
def vote(request, poll_id):
    if request.method == 'GET':
        return Http404("Page Not Found")
    elif request.method == 'POST':
        # getting the question the user voted and storing it in cache for subsequent queries
        question = get_object_or_404(Question, id=poll_id) 

        # checking if the user has voted on this question
        if f'voted_{question.id}' in request.session:
            return HttpResponse("You have already voted. You cannot vote again.")
        else:
            choice = get_object_or_404(question.choice_set, id=request.POST["choice"])
            choice.votes += 1
            choice.save()
            request.session[f'voted_{question.id}'] = True  # Marking the question as voted in the session
            return redirect(reverse('resultpage', args=(choice.question.id,)))

@require_http_methods(["GET", "POST"])
def name_form_view(request):
    if request.method == "GET":
        form = BasicForm()
        return render(request, 'form.html', context={'form': form})
    elif request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            # Here you can process the form data as needed
            return HttpResponse("thanks for submitting data to this endpoint")
        else:
            return render(request, 'form.html', context={'form': form})

# using model forms
# By making use of the Book and Author models from UsingModels lesson,
# this is a view that creates a form that is used to change or create author and book instances in the database

def create_author(request):
    if request.method == "GET": 
        # this is used if we need to create new author
        new_author_form = AuthorForm()

        # to edit data for an existing author we make use of this view
        author = Author.objects.get(id=15)
        new_author_form = AuthorForm(instance=author)
        return render(request, 'form.html', context={'form': new_author_form})
    else:
        return HttpResponse("New Author created successfully")

@require_GET
def create_book(request):
    # to create a form for a new book
    new_book = BookForm()
    return render(request, 'form.html', {'form': new_book})

