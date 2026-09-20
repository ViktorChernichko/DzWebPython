from django.urls import path

from . import views

urlpatterns = [
    path("number/", views.random_number),
    path("range/", views.random_in_range),
    path("set/", views.random_set),
]
