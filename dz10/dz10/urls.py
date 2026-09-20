from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('writers/', views.writers, name='writers'),
    path('writers/<str:name>/', views.writer_detail, name='writer_detail'),
    path('writers/<str:name>/<str:book_key>/', views.writer_book, name='writer_book'),

    path('books/', views.books, name='books'),
    path('books/<int:position>/', views.book_by_position, name='book_by_position'),

    path('cities/', views.writers, name='cities'),
]
