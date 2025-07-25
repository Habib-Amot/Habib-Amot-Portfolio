from django import forms
from UsingModels.models import Book
from django.utils.translation import gettext_lazy as _

class NameForm(forms.Form):
    my_name = forms.CharField(label="Enter your Name:", max_length=100, min_length=6, help_text='enter your name')
    # i can alsoe add another CharField to this form but with different widget
    about_me = forms.CharField(label="Enter Your Bio", widget=forms.Textarea(
        attrs={'class': 'user-bio', 'width': "200px", 'height': '150px'})
    )
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


# this form is a model form that allows for changing and validating data regarding books that is being uploaded
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price']
        labels = {
            'title': _('this is the title of the book')
        }
