from rest_framework import serializers
from .models import *



class WeatherSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Weather
        fields = '__all__'