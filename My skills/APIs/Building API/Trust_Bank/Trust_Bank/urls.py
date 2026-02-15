from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    # this url endpoints are meant to be browsable i.e. they are meant to be interacted with by humans
    re_path(r'^(?:home[/]?)?$', include('applications.urls_router')),
    path('app/', include('applications.urls_router')),
    path('admin/', admin.site.urls),

    # this is points the url endpoints for APIs i.e. they are meant to be used by application and not by human
    path('api/', include('applications.api_url_router')),
]
