from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(f'this are the properties of the request that was sent to the server {request.META}')
