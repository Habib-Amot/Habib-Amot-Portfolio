# this form is used to collect information from users, especially messages and then it's going to send the email message to the recipient

from django import forms

class EmailMessageForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'resize':'both'}))
    recipient_email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EmailAttachmentForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'resize':'both'}))
    recipient_email = forms.EmailField()
    attachment = forms.FileField(required=True, label='attach file')

    