# apis.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal
from .serializers import MealSerializer

class MealListAPIView(APIView):
    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

class MealCreateAPIView(APIView):
    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealDeleteAPIView(APIView):
    def post(self, request):
        meal_id = request.data.get('meal_id')
        try:
            meal = Meal.objects.get(id=meal_id)
            meal.delete()
            return Response({"message": "Meal deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Meal.DoesNotExist:
            return Response({"error": "Meal not found"}, status=status.HTTP_404_NOT_FOUND)

class MealUpdateAPIView(APIView):
    def post(self, request, meal_id):
        try:
            meal = Meal.objects.get(id=meal_id)
            serializer = MealSerializer(meal, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Meal.DoesNotExist:
            return Response({"error": "Meal not found"}, status=status.HTTP_404_NOT_FOUND)
