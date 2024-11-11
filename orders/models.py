from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from meals.models import Meal

from django.db import models
from meals.models import Meal

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Total: ${self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.meal.name}"

