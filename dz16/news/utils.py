from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme


def paginate(request, queryset, per_page):
    return Paginator(queryset, per_page).get_page(request.GET.get("page"))


def redirect_back(request, fallback, *fallback_args):
    next_url = request.POST.get("next", "")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)
    return redirect(fallback, *fallback_args)
