from rest_framework import permissions
from rest_framework.permissions import BasePermission

from rest_framework_api_key.permissions import HasAPIKey

from applications.users.models import UserAPIKey

class IsAuthenticatedOrHasAPIKey(BasePermission):
               
    def has_permission(self, request, view) -> bool:
        # first is to check if the user is authenticated
        if request.user and request.user.is_authenticated:
            return True
        
        key = request.META.get("X-API-KEY")
        if key:
            try:
                user = UserAPIKey.objects.get_from_key(key).user
                request.user = user
                return True
            except UserAPIKey.DoesNotExist:
                return False
        return False
    