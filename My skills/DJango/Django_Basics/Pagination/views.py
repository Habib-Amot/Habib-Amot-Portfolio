from django.shortcuts import render
from django.core.paginator import Paginator
from UsingModels.models import Author

# Create your views here.

def author_view(request):
    authors = Author.objects.all()
    paginated_author_list = Paginator(authors, 5, orphans=4)

    # getting the page number of the author from the url and defaulting to 1 if none is passed
    try:
        page_number = int(request.GET.get('page', 1))
        author_page = paginated_author_list.get_page(page_number)
        return render(request, 'author-pagination.html', {'author_page': author_page})
    except ValueError:
        page_number = 1
