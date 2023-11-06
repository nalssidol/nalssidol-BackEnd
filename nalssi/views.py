from .models import Weather
from .serializers import WeatherSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action

#1. 날씨 ViewSet
class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()

    @action(methods=['POST'], detail=True)
    def clothes(self, request, pk=None):
        temperature = self.get_object() # 온도 불러오기