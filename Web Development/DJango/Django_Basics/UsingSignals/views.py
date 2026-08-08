from django.shortcuts import render
from django.core.signals import request_started, request_finished
from django.db.models.signals import post_save 
from django.dispatch import receiver, Signal
from django.http import HttpResponse
from datetime import datetime
# for the sake of learning and practice, I am going to make use of the A
# Create your views here.
# for testing sake, I am going to be making use of a simple view that returns just a line of text and then call the request started signal
# and then call the request finished signals after it has finished running
# this signals will be used to record the time it takes for a particular view to finish running

def simple_view(request):
    # mimicking a post save signal that is being sent from within this function 
    Signal.send(post_save, sender=simple_view)
    return HttpResponse('this is a very simple view that makes use of django signals')

# this approach is not the best approach to make use of signal handlers
# as this might cause some import issues and will result in the handles to registered more than once
# but I am including this here for the sake of learning
@receiver([request_started, request_finished])
def log_starttime(*args, **kwargs):
    print(f'request start at {datetime.now()}')


@receiver(post_save, sender=simple_view)
def log_post_save(*args, **kwargs):
    print("this signal is gotten from calling the post_save signal") 

