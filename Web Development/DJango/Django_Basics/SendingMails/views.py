from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.views.generic import View
from django.http import HttpResponse
from smtplib import SMTPDataError, SMTPConnectError, SMTPAuthenticationError, SMTPException
from .forms import EmailMessageForm, EmailAttachmentForm

# Create your views here.

# this app is actually about sending of emails to recipient(s)
class EmailUser(View):
    def get(self, request, *args, **kwargs):
        form = EmailMessageForm()
        return render(request, 'email-sender.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        data = EmailMessageForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data['first_name']
            message = data.cleaned_data['message']
            message += f"\n\n<h3 style='color:red, text-decoration:underline'>This message was sent by {name} using Django Basics Email Sender App.</h3>"
            email_address = data.cleaned_data['recipient_email']
            subject = f"Message from {name}"
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=None,  # Use default from email configured in settings
                    recipient_list=[email_address],
                    fail_silently=False,
                )
                return HttpResponse("Email sent successfully!")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except (SMTPDataError, SMTPConnectError, SMTPAuthenticationError, SMTPException) as e:
                return HttpResponse(f"An error occurred while sending the email: {str(e)}")
            except Exception as e:
                return HttpResponse(f"An unexpected error occurred: {str(e)}")
        else:
            return HttpResponse("the data you entered is invalid")

# and this view involves sending emails that contains attachments to user(s)
class EmailWithAttachment(View):
    def get(self, request, *args, **kwargs):
        form = EmailAttachmentForm()    
        return render(request, 'email-attachment.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        data = EmailMessageForm(request.POST, request.FILES)
        if data.is_valid():
            name = data.cleaned_data['first_name']
            message = data.cleaned_data['message']
            message += f"\n\n<h3 style='color:red, text-decoration:underline'>This message was sent by {name} using Django Basics Email Sender App.</h3>"
            email_address = data.cleaned_data['recipient_email']
            subject = f"Message from {name}"
            attachment = request.FILES.get('attachment')
            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,  # Use default from email configured in settings
                    to=[email_address],
                )
                if attachment:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                    email.content_subtype = 'html'  # Set content type to HTML if needed
                email.send(fail_silently=False)
                return HttpResponse("Email with attachment sent successfully!")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except (SMTPDataError, SMTPConnectError, SMTPAuthenticationError, SMTPException) as e:
                return HttpResponse(f"An error occurred while sending the email: {str(e)}")
            except Exception as e:
                return HttpResponse(f"An unexpected error occurred: {str(e)}")
        else:
            return HttpResponse("the data you entered is invalid")
