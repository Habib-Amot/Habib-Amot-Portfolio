# this is a custom preprocessor that returns the email of our website
from django.conf import settings
def siteEmail(request):
    site_email = {'SITE_EMAIL': settings.SITE_TEMPLATE_EMAIL}
    return site_email