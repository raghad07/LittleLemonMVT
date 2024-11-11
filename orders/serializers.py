# serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from meals.models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'price']  # Adjust fields as necessary

class OrderItemSerializer(serializers.ModelSerializer):
    meal = MealSerializer()  # Nested serializer for meal

    class Meta:
        model = OrderItem
        fields = ['meal', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)  # List of order items
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # To return total price

    class Meta:
        model = Order
        fields = ['id', 'order_items', 'total_price', 'order_status', 'created_at']
