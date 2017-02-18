from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from .middleware import _SESSION_KEY

@user_passes_test(lambda u: u.is_superuser)
def runas_enter(request, user_id):
    """
    Begins impersonating a user by adding the new user's ID to the session, so
    the `RunAsMiddleware` can replace the user object on each request.

    Only a superuser may impersonate another user.
    """

    # validate the user object is correct and is not the current user
    new_user = get_object_or_404(User, pk=user_id)
    if new_user.id == request.user.id:
        return HttpResponseBadRequest('You cannot impersonate yourself')

    request.session[_SESSION_KEY] = new_user.id
    messages.success(request, 'runas: now impersonating user {}'.format(new_user.username))

    return redirect('/')

def runas_exit(request):
    """
    Exits impersonation mode by deleting the session variable. The middleware
    will not apply to further requests.
    """

    user_admin_page = None

    if _SESSION_KEY in request.session:
        user_admin_page = reverse('admin:auth_user_change', 
                args=[request.session[_SESSION_KEY]])
        del request.session[_SESSION_KEY]
        messages.success(request, 'runas: no longer impersonating user {}'.format(request.user.username))

    return redirect(user_admin_page or '/')
