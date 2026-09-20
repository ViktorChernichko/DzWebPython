from django.urls import path
from . import views

app_name = 'dz13'

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('create/', views.restaurant_create, name='restaurant_create'),
    path('<int:restaurant_id>/edit/', views.restaurant_update, name='restaurant_update'),
    path('<int:restaurant_id>/delete/', views.restaurant_delete, name='restaurant_delete'),
]
