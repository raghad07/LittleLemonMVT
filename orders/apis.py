# api.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, MealSerializer
from meals.models import Meal

class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            meal_id = request.data.get('meal')
            quantity = request.data.get('meal_quantity', 1)
            
            # Retrieve the meal
            meal = Meal.objects.get(id=meal_id)
            
            # Create an order
            order = Order.objects.create()
            order_item = OrderItem.objects.create(order=order, meal=meal, quantity=quantity)
            
            # Calculate the total price for the order
            total_price = meal.price * quantity
            order.total_price += total_price
            order.save()
            
            return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)
        
        except Meal.DoesNotExist:
            return Response({"error": "Meal not found"}, status=status.HTTP_400_BAD_REQUEST)

class OrderHistoryView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        order_summary = []

        for order in orders:
            total_order_price = 0
            order_items_data = []
            for item in order.order_items.all():
                total_order_price += item.meal.price * item.quantity
                order_items_data.append({
                    'meal': MealSerializer(item.meal).data,
                    'quantity': item.quantity,
                    'total_item_price': item.meal.price * item.quantity
                })

            order_summary.append({
                'order': OrderSerializer(order).data,
                'total_order_price': total_order_price,
                'order_items': order_items_data
            })
        
        return Response(order_summary, status=status.HTTP_200_OK)
