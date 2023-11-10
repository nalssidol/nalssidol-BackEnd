from rest_framework import serializers
from .models import *



class WeatherSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Weather
        fields = '__all__'
    
    dol = serializers.ImageField(use_url=True, required=False)