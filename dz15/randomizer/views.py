import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET

DEFAULT_MIN = 0
DEFAULT_MAX = 100
MAX_COUNT = 1000


def parse_int(request, name, default):
    raw = request.GET.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"Parameter '{name}' must be an integer.")


def error(message):
    return JsonResponse({"error": message}, status=400)


@require_GET
def random_number(request):
    return JsonResponse({"number": random.randint(DEFAULT_MIN, DEFAULT_MAX)})


@require_GET
def random_in_range(request):
    try:
        low = parse_int(request, "min", DEFAULT_MIN)
        high = parse_int(request, "max", DEFAULT_MAX)
    except ValueError as exc:
        return error(str(exc))
    if low > high:
        return error("Parameter 'min' must not be greater than 'max'.")
    return JsonResponse({"min": low, "max": high, "number": random.randint(low, high)})


@require_GET
def random_set(request):
    try:
        low = parse_int(request, "min", DEFAULT_MIN)
        high = parse_int(request, "max", DEFAULT_MAX)
        count = parse_int(request, "count", 10)
    except ValueError as exc:
        return error(str(exc))
    if low > high:
        return error("Parameter 'min' must not be greater than 'max'.")
    if count < 1 or count > MAX_COUNT:
        return error(f"Parameter 'count' must be between 1 and {MAX_COUNT}.")
    numbers = [random.randint(low, high) for _ in range(count)]
    return JsonResponse({"min": low, "max": high, "count": count, "numbers": numbers})
