from accounts.utils import is_portal_admin

from .models import SiteSettings


def portal(request):
    return {
        "site_settings": SiteSettings.load(),
        "is_portal_admin": is_portal_admin(request.user),
    }
