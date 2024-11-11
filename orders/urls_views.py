from meals import views
from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views
  

urlpatterns = [
    path('order/', views.create_order, name='place_order'),  
    path('order/history/', views.order_history, name='order_history'),  
]











