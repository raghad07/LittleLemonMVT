# urls.py
from django.urls import path
from . import apis

urlpatterns = [
    path('meal/list/', apis.MealListAPIView.as_view(), name='meal_list_api'),
    path('meal/add/', apis.MealCreateAPIView.as_view(), name='add_meal_api'),
    path('meal/delete/', apis.MealDeleteAPIView.as_view(), name='delete_meal_api'),
    path('meal/update/<int:meal_id>/', apis.MealUpdateAPIView.as_view(), name='update_meal_api'),
]
