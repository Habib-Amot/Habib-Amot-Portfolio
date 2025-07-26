from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Max
from django.shortcuts import render
from UsingModels.models import Author

# Create your views here.
# this files holds views that are just meant for handling and rendering templates 

# for example here in our view, we are going to render some author details and also the number of books they have written
def show_template(request):
    # first I am going to take each author and then annotate the number of books they they have written to each author and also the highest price of their book
    # we might also be interested in showing authors top book rating and likes
    annotated_author = Author.objects.annotate(book_count=Count('book', distinct=True), highest_book_price=Max('book'), top_review=Max('book__review'), top_rated=Max('book__rating'))


    # now we have to pass this data into our template and render the data
    return render(request, 'home.html', context={'authors': annotated_author})

