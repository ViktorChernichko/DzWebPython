from django.urls import path

from . import views

urlpatterns = [
    path("", views.random_fortune),
    path("all/", views.all_fortunes),
]
