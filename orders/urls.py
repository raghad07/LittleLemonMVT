# urls.py
from django.urls import path
from . import apis

urlpatterns = [
    path('order/create/', apis.CreateOrderView.as_view(), name='create_order_api'),
    path('order/history/', apis.OrderHistoryView.as_view(), name='order_history_api'),
]
