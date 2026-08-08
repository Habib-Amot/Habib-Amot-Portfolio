from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# modelling form views here

# this form is for receiving user login details before authenticating them
class AuthorForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter Your username')
    password = forms.CharField(label="Enter Your Password", widget=forms.PasswordInput())



class AuthorRegistrationForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.field_order = ['username', 'password', 'confirm_password','email', 'agree_to_terms']
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = { 
            "username": "Enter your Username",
            'password': "Enter your password",
            'email': "Enter your email address"
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    # calling other field that is need for the registration process
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(), label="Confirm Password")
    agree_to_terms = forms.BooleanField(required=True, widget=forms.CheckboxInput(), label="agree to our terms and condition")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        confirm_password = cleaned_data.get('confirm_password', None)

        if (password and confirm_password) and confirm_password == password:
            return cleaned_data
        else:
            self.errors["password"] = "password mismatch"
            return cleaned_data
