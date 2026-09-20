from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("random/", views.random_poem),
    path("random/author/<str:author>/", views.random_poem_by_author),
    path("random/theme/<str:theme>/", views.random_poem_by_theme),
    path("authors/", views.authors),
    path("themes/", views.themes),
    path("author/<str:author>/titles/", views.titles_by_author),
    path("theme/<str:theme>/titles/", views.titles_by_theme),
]
