#  this middleware is used to handle the site under maintenance
# all request that is made during  maintenance will be blocked by this middleware

from django.http import HttpResponse
from django.conf import settings

class SiteUnderMaintenanceMiddleware:
    """
    Middleware to block all requests when the site is under maintenance.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if getattr(settings, 'SITE_UNDER_MAINTENANCE', False) and request.user.is_admin is False:
                return HttpResponse("<h1>The site is currently under maintenance. Please try again later.</h1>", status=503)
        except AttributeError:
            # Handle the case where request.user does not have is_admin attribute
            return HttpResponse("<h1>The site is currently under maintenance. Please try again later.</h1>", status=503)
        else:
            response = self.get_response(request)
            return response
