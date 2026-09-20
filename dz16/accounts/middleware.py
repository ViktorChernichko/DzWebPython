from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

from .utils import describe_ban, get_active_ban


class BanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            ban = get_active_ban(user)
            if ban:
                logout(request)
                messages.error(request, describe_ban(ban))
                return redirect("accounts:login")
        return self.get_response(request)
