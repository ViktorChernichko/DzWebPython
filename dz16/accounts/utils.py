from datetime import timedelta

from django.db.models import Q
from django.utils import timezone

ADMIN_GROUP_NAME = "Portal Administrators"

BAN_DURATIONS = {
    "day": timedelta(days=1),
    "week": timedelta(weeks=1),
    "month": timedelta(days=30),
    "forever": None,
}


def is_portal_admin(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return user.groups.filter(name=ADMIN_GROUP_NAME).exists()


def active_bans():
    from .models import Ban

    return Ban.objects.filter(lifted=False).filter(
        Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now())
    )


def get_active_ban(user):
    return active_bans().filter(user=user).order_by("-created_at").first()


def describe_ban(ban):
    if ban.expires_at is None:
        text = "Your account is permanently banned."
    else:
        local = timezone.localtime(ban.expires_at)
        text = f"Your account is banned until {local:%Y-%m-%d %H:%M}."
    if ban.reason:
        text += f" Reason: {ban.reason}"
    return text
