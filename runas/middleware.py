"""
Middleware to support impersonating a user.

Django 1.10 changes the middleware style. For now, we use the provided
mixin to provide backwards compatibility for both styles of middleware.
"""

from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

_SESSION_KEY = '_runas_id'

class RunAsMiddleware(MiddlewareMixin):
    """
    Detects if the impersonation token is present in the session, and if so,
    replaces the logged on user instance with the impersonated user. This
    happens on every request, so to "undo", simply delete the session
    variable.

    Only superusers are allowed to impersonate other users.
    """

    def process_request(self, request):
        if request.user.is_superuser and _SESSION_KEY in request.session:
            new_user = User.objects.get(pk=request.session[_SESSION_KEY])
            if new_user is not None:
                request.user = new_user
