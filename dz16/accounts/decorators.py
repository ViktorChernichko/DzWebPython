from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .utils import is_portal_admin


def portal_admin_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not is_portal_admin(request.user):
            raise PermissionDenied
        return view(request, *args, **kwargs)

    return login_required(wrapper)
