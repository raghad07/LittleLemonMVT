from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderItemForm
from meals.models import Meal


def create_order(request):
    meals = Meal.objects.all()  
    if request.method == "POST":
        order = Order.objects.create() 
        total_price = 0

        meal_id = request.POST.get('meal')  
        quantity = int(request.POST.get('meal_quantity', 1)) 
        
        meal = Meal.objects.get(id=meal_id)

        order_item = OrderItem.objects.create(order=order, meal=meal, quantity=quantity)

        total_price += meal.price * quantity
        order.total_price += total_price  
        order.save()
        
        return redirect('order_history')  

    return render(request, 'place_order.html', {'meals': meals})

def order_history(request):
    orders = Order.objects.all()
    order_summary = [] 

    for order in orders:
        total_order_price = 0
        for item in order.order_items.all():
            total_order_price += item.meal.price * item.quantity
        order_summary.append({
            'order': order,
            'total_order_price': total_order_price,
        })

    return render(request, 'order_history.html', {'order_summary': order_summary})
