from django.urls import path

from . import views

app_name = "panel"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("articles/", views.article_list, name="article_list"),
    path("articles/create/", views.article_create, name="article_create"),
    path("articles/<int:pk>/edit/", views.article_edit, name="article_edit"),
    path("articles/<int:pk>/delete/", views.article_delete, name="article_delete"),
    path("users/", views.user_list, name="user_list"),
    path("users/create/", views.user_create, name="user_create"),
    path("users/<int:pk>/delete/", views.user_delete, name="user_delete"),
    path("users/<int:pk>/ban/", views.user_ban, name="user_ban"),
    path("users/<int:pk>/unban/", views.user_unban, name="user_unban"),
    path("comments/", views.comment_list, name="comment_list"),
    path("comments/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
    path("appearance/", views.appearance, name="appearance"),
    path("statistics/", views.statistics, name="statistics"),
]
