from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView,FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Count, Max
from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from WorkingWithForms.forms import NameForm, AuthorForm
from UsingModels.models import Author

# Create your views here.
class Home(View):
    form_class = NameForm
    template_name = 'name.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, template_name=self.template_name, context={'form':form})
    
    def post(self, request):
        submitted_data = self.form_class(request.POST)
        if submitted_data.is_valid():
            return HttpResponse("thanks for submitting your data")

class AuthorView(ListView):
    queryset = Author.objects.annotate(book_count=Count('book', distinct=True), highest_book_price=Max('book'), top_review=Max('book__review'), top_rated=Max('book__rating'))

    template_name = 'home.html'
    context_object_name = 'authors'

class AuthorDetails(DetailView):
    model = Author
    template_name = 'details.html'
    context_object_name = 'author'
    queryset = Author.objects.annotate(book_count=Count('book', distinct=True), highest_book_price=Max('book'), top_review=Max('book__review'), top_rated=Max('book__rating'))

class AuthorLogin(FormView):
    form_class = AuthorForm
    template_name = 'author-login.html'
    success_url = reverse_lazy('author-cbv')

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']     
    template_name = 'author-create.html' 
    success_url = reverse_lazy('author-cbv')

# using Mixins to handle request and add flexibilty
# first I am going to make use of SingleObjectMixin to display a single object from the database
class AuthorMixin(SingleObjectMixin, View):
    model = Author
    
    def get(self, request, *args, **kwargs):
        # getting the object with the pk that is provided in the url
        Object =  self.get_object()
        return HttpResponse("this is the id of the given author {}".format(Object.pk))

# mixins can be used to effect the way a View is rendered and processed
# for example, this view will take a single author and then return the details of the books that the author has written
class SingleAuthorBooks(SingleObjectMixin, ListView):
    template_name = 'publisher_detail.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        # getting the single author that whose book will be returned, 
        self.object = self.get_object(queryset=Author.objects.all())

        # further calling the get method that is defined in the ListView class
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        return self.object.book_set.all()

# so lets create an AjaxResponseMixin
# this mixin takes an author ui by subclassing the SingleObjectMixin the checks if the author is authenticated and returns the details of the Author in Ajax form
class AuthorDetailsAjaxResponseMixin(SingleObjectMixin):
    def get(self, request, *args, **kwargs):
        # getting the author that we want to return ajax details for
        self.author_objects = self.get_object(queryset=Author.objects.all())

        # building the author details
        data = {
            'author_name': self.author_objects.name,
            'author_age': self.author_objects.age,
            'no_of_book': self.author_objects.book_set.count(),
            'top_price': f"${self.author_objects.book_set.aggregate(max_price=Max('price'))['max_price']}"
        }
        return JsonResponse(data=data)

# now we cn use the Mixin with our View
class AuthorAjaxResponse(AuthorDetailsAjaxResponseMixin, View):
    pass
