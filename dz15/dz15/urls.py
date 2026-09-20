from django.http import JsonResponse
from django.urls import include, path


def index(request):
    return JsonResponse(
        {
            "project": "dz15",
            "endpoints": {
                "fortune": "/api/fortune/",
                "random_number": "/api/random/number/",
                "random_range": "/api/random/range/?min=1&max=10",
                "random_set": "/api/random/set/?count=5&min=1&max=100",
                "poems": "/api/poems/",
            },
        }
    )


urlpatterns = [
    path("", index),
    path("api/fortune/", include("fortune.urls")),
    path("api/random/", include("randomizer.urls")),
    path("api/poems/", include("poems.urls")),
]
