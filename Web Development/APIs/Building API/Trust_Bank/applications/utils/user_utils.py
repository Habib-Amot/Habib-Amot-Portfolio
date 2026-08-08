# this utilily class is used for common functions and classes that are used by the application

from django.core.signing import loads, dumps

# annotation importation
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User

def generate_email_verification_link(user: User, request: HttpRequest) -> tuple:
    user_key = user.objects.get('pk')
    signed_key = dumps(user_key)

    # reversing the url that will be attached to the link
    relative_url = reverse('verification-endpoint', kwargs={'token': signed_key})

    # building the full url
    absolute_url = request.build_absolute_uri(relative_url)
    return signed_key, absolute_url