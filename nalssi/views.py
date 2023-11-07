from .models import Weather
from .serializers import WeatherSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView


@api_view(['GET'])
def temperature_grade(request, temperature):
    try:
        temperature = float(temperature)
        if temperature >= 0 and temperature <= 5:
            grade = "A"
        elif temperature > 5 and temperature <= 10:
            grade = "B"
        else:
            grade = "Unknown"
        
        data = {"temperature": temperature, "grade": grade}
        
        return Response(data)
    except ValueError:
        return Response({"error": "Invalid temperature value"}, status=400)