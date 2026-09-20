import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .data import FORTUNES


@require_GET
def random_fortune(request):
    return JsonResponse({"fortune": random.choice(FORTUNES)})


@require_GET
def all_fortunes(request):
    return JsonResponse({"count": len(FORTUNES), "fortunes": FORTUNES})
