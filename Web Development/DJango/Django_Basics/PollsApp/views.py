from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView, ListView
from .models import Question, Choice

# Create your views here.
# this view is the index page that shows all the polls that is available on our site
class home(ListView):
    template_name = 'polls/home.html'
    context_object_name = 'question_list'
    model = Question 
    
    def query_set():
        return Question.objects.all()


# this shows the detail of a particular question
# this includes the question as well as the choices
class detail(DetailView):
    model = Question
    template_name = 'polls/details.html'
    context_object_name = 'question'


class result(DetailView):
    model = Question
    template_name = 'polls/result.html'
    context_object_name = "question"


def vote(request, poll_id):
    if request.method == "GET":
        return Http404("page Not found ")
    else:
        choice = get_object_or_404(Choice, id=request.POST["choice"])
        choice.votes += 1
        choice.save()
        return redirect(f"/polls/result/{choice.question.id}")
