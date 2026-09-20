from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('news/', views.news, name='news'),
    path('news/<path:extra>', views.news, name='news_extra'),

    path('management/', views.management, name='management'),
    path('management/<path:extra>', views.management, name='management_extra'),

    path('facts/', views.facts, name='facts'),
    path('facts/<path:extra>', views.facts, name='facts_extra'),

    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<path:extra>', views.contacts, name='contacts_extra'),

    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
    path('history/', views.history, name='history'),
    path('history/<path:extra>', views.history, name='history_extra'),
]
