import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from UsingModels.models import Author, Publisher

# Create your views here.

# so I am going to create a view that involves some complex and time consuming process 
# so we are going to see the cache in action 

@cache_page(60 * 10) # caching the result of the page for 10 minuttes
def complex_view(request):
    # this view will take about 20 secs for it to crespond
    time.sleep(20)
    return HttpResponse("finally we have the result of our view, this could have taken about 20 seconds but if you see this earlier <br> it's been sent by the Cache")

# this view will take time with the initial request as there is a process inside this view that requires more time to compute
# this action can be significantly cut off to less response time
def long_running_task(request, toggle=0):
    # the toggle is used to determine if the cache should be deleted or not
    # we have a list of authors that we want to show as well as the length of their names
    authors = Author.objects.all()
    cache.delete('author-details') if toggle else None 
    author_details = cache.get("author-details", None)
    if author_details:
        return HttpResponse(f'{author_details}')
    else:
        time.sleep(20)
        author_details = {author.name:author.age for author in authors}
        cache.set('author-details', author_details, 600)
        return HttpResponse(f'{author_details}')

# and finally, this view is used for template caching 
def template_cache(request):
    return render(request, 'template-cache.html', {'Publisher': Publisher.objects.all()})
