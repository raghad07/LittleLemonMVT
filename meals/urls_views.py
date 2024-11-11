from meals import views
from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('meal/lista', views.list_all, name='meal_list'),  
    path('meal/add/', views.add_meal, name='add_meal'),  
    path('remove/<int:meal_id>/', views.confirm_delete_meal, name='confirm_delete_meal'), 

    path('meal/delete/', views.delete_meal, name='delete_meal'),
    path('update/<int:meal_id>/', views.update_meal, name='update_meal'),

]




