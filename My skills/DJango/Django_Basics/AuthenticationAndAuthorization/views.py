from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate

from .forms import AuthorRegistrationForm, LoginForm

# Create your views here.
def home(request):
    return HttpResponse('this is the home page for all users')


class Register(View):
    template_name = 'register-user.html'
    def get(self, request, *args, **kwargs):
        form = AuthorRegistrationForm()
        return render(request, template_name=self.template_name, context={'form': form})
    def post(self, request, *args, **kwargs):
        sumitted_data = AuthorRegistrationForm(request.POST)
        if sumitted_data.is_valid():
            user = sumitted_data.save()
            login(request, user)
            return redirect(reverse('user-dashboard'))
        else:
            return render(request, template_name=self.template_name, context={'form': sumitted_data})


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(
            request=request, template_name='login.html', context={'form':form}
        )
    else:
        submitted_data = LoginForm(request.POST)
        if submitted_data.is_valid():
            username = submitted_data.cleaned_data['username']
            password = submitted_data.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('user-dashboard'))
            else:
                return HttpResponse('invalid login credentials provided')
            
        return HttpResponse('invalid login data provided')
    
    
def user_logout(request):
    logout(request)
    return redirect(reverse('user-login'))

@login_required(login_url=reverse_lazy('user-login'))
def dashboard(request):
    return HttpResponse('this is the dashboard <br> <a href="{}">view users</a> <a href="{}">logout</a>'.format(reverse('all-users-view'), reverse('user-logout')))


# creating a view that can only be accessed by users who has the permission to view all users
# but first they must be logged in
@login_required(login_url=reverse_lazy('user-login'))
@permission_required('auth.can_view_users', raise_exception=True)
def all_users(request):
    return HttpResponse('this is the view for all users, only accessible by users with the permission to view all users')
