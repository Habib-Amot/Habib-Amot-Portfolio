# this contains the forms that are being used in the views
from django.forms import Form
from django import forms
from .models import SiteUser
from UsingModels.models import Author, Book

class RegistrationForm(Form):
    # Define your form fields here
    username = forms.CharField(max_length=100, required=True, label='username')
    email = forms.EmailField(required=True, label='Email Field')
    profile_picture = forms.FileField(required=True, label='Profile Picture')
    bio = forms.CharField(widget=forms.Textarea, required=False, label='Bio')

class AdminRegister(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ['username', 'email', 'profile_picture', 'first_name', 'last_name', 'password']
    
class BasicForm(Form):
    name = forms.CharField(max_length=2, label="enter your name", required=True)
    age = forms.IntegerField(label="enter your age", required=True)
    id = forms.HiddenInput(attrs={'value': '12345'})

# modeling a form for an existing object
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'age']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'price', 'rating', 'review', 'pub_date', 'publisher']
    
# class MultipleFileUploadForm(forms.ModelForm):
#     files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True, label='Upload Files')
#     # tests = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
