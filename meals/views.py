from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest,HttpResponse
from .forms import MealForm
from .models import Meal


def list_all(request):
    meals = Meal.objects.all()
    
    return render(request, 'meals.html', {'meals': meals})

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'add_meal.html', {'form': form})


def confirm_delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)  
    return render(request, 'confirm_delete.html', {'meal': meal})  

def delete_meal(request):
    if request.method == 'POST':
        meal_id = request.POST.get('meal_id') 
        meal = get_object_or_404(Meal, id=meal_id)  
        meal.delete()  
        return redirect('meal_list')  
    return redirect('meal_list')  


def update_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)  

    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal) 
        if form.is_valid():
            form.save()  
            return redirect('meal_list')  
    else:
        form = MealForm(instance=meal)  

    return render(request, 'update_meal.html', {'form': form, 'meal': meal})  






