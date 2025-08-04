# this file contains some custom signals that is going to be consumed by receivers in my view

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.signals import request_started
from django.contrib.auth.models import User

from .models import UserProfile

@receiver(post_save)
def post_save_receiver(sender, **kwargs):
    print(sender)
    print("i was called because a post save action has happened")


@receiver(request_started)
def log_request_start(*args, **kwargs):
    print('this signal handler was called because a view has started')

# this signal is called anytime and user profile is being created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # checking if this user was just created or not 
    if created:
        UserProfile.objects.create(user=instance)
        print(f'new user profile has been created for {instance.username}')
    else:
        print("no user has been created whatsoever")
