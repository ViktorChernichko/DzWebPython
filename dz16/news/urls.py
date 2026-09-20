from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("articles/<int:pk>/", views.article_detail, name="article_detail"),
    path("articles/<int:pk>/save/", views.toggle_save, name="toggle_save"),
    path("saved/", views.saved_list, name="saved_list"),
]
