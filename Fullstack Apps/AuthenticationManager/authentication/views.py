from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, 'authentication/templates/login.html')
    else:
        return HttpResponse("this request is made with a methof that is not Get")
