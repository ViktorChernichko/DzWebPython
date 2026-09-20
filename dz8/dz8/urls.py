from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('table/', views.multiplication_table, name='multiplication_table'),
    path('programmers-day/', views.programmers_day, name='programmers_day'),
]
