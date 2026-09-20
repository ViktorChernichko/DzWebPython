import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .data import POEMS


def find_case_insensitive(values, wanted):
    wanted = wanted.strip().lower()
    for value in values:
        if value.lower() == wanted:
            return value
    return None


def all_authors():
    return sorted({poem["author"] for poem in POEMS})


def all_themes():
    return sorted({theme for poem in POEMS for theme in poem["themes"]})


def serialize(poem):
    return {
        "title": poem["title"],
        "author": poem["author"],
        "themes": poem["themes"],
        "text": poem["text"],
    }


def not_found(message):
    return JsonResponse({"error": message}, status=404)


@require_GET
def index(request):
    return JsonResponse(
        {
            "endpoints": {
                "random_poem": "/api/poems/random/",
                "random_poem_by_author": "/api/poems/random/author/<author>/",
                "random_poem_by_theme": "/api/poems/random/theme/<theme>/",
                "authors": "/api/poems/authors/",
                "themes": "/api/poems/themes/",
                "titles_by_author": "/api/poems/author/<author>/titles/",
                "titles_by_theme": "/api/poems/theme/<theme>/titles/",
            }
        }
    )


@require_GET
def random_poem(request):
    return JsonResponse(serialize(random.choice(POEMS)))


@require_GET
def random_poem_by_author(request, author):
    name = find_case_insensitive(all_authors(), author)
    if name is None:
        return not_found(f"Author '{author}' was not found.")
    poems = [poem for poem in POEMS if poem["author"] == name]
    return JsonResponse(serialize(random.choice(poems)))


@require_GET
def random_poem_by_theme(request, theme):
    name = find_case_insensitive(all_themes(), theme)
    if name is None:
        return not_found(f"Theme '{theme}' was not found.")
    poems = [poem for poem in POEMS if name in poem["themes"]]
    return JsonResponse(serialize(random.choice(poems)))


@require_GET
def authors(request):
    return JsonResponse({"authors": all_authors()})


@require_GET
def themes(request):
    return JsonResponse({"themes": all_themes()})


@require_GET
def titles_by_author(request, author):
    name = find_case_insensitive(all_authors(), author)
    if name is None:
        return not_found(f"Author '{author}' was not found.")
    titles = [poem["title"] for poem in POEMS if poem["author"] == name]
    return JsonResponse({"author": name, "titles": titles})


@require_GET
def titles_by_theme(request, theme):
    name = find_case_insensitive(all_themes(), theme)
    if name is None:
        return not_found(f"Theme '{theme}' was not found.")
    titles = [poem["title"] for poem in POEMS if name in poem["themes"]]
    return JsonResponse({"theme": name, "titles": titles})
