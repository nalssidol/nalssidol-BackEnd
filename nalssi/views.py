from .models import Weather
from .serializers import WeatherSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView


@api_view(['GET'])
def temperature_recommend(request, temperature): # temperature 파라미터 프론트에서 가져오기
    try:
        temperature = float(temperature)
        # 아우터 추천
        if temperature >= -30 and temperature <= 4:
            outer = "패딩, 두꺼운 코트, 누빔 옷"
        elif temperature > 4 and temperature <= 8:
            outer = "울 코트, 가죽 옷"
        elif temperature > 8 and temperature <= 11:
            outer = "트렌치 코트, 야상, 점퍼"
        elif temperature > 11 and temperature <= 16:
            outer = "자켓, 가디건, 청자켓"
        elif temperature > 16 and temperature <= 19:
            outer = "얇은 가디건"
        elif temperature > 19 and temperature <= 22:
            outer = "X"
        elif temperature > 22 and temperature <= 27:
            outer = "X"
        elif temperature > 28 and temperature <= 50:
            outer = "X"
        else:
            outer = "Unknown"
        
        # 상의 추천
        if temperature >= -30 and temperature <= 4:
            upper = "니트, 맨투맨, 후드"
        elif temperature > 4 and temperature <= 8:
            upper = "니트, 맨투맨, 후드"
        elif temperature > 8 and temperature <= 11:
            upper = "니트, 맨투맨, 후드"
        elif temperature > 11 and temperature <= 16:
            upper = "니트, 맨투맨, 후드"
        elif temperature > 16 and temperature <= 19:
            upper = "니트, 맨투맨, 후드"
        elif temperature > 19 and temperature <= 22:
            upper = "블라우스, 긴팔 티"
        elif temperature > 22 and temperature <= 27:
            upper = "반팔, 얇은 셔츠"
        elif temperature > 28 and temperature <= 50:
            upper = "민소매, 반팔"
        else:
            upper = "Unknown"

        # 하의 추천
        if temperature >= -30 and temperature <= 4:
            lower = "기모바지"
        elif temperature > 4 and temperature <= 8:
            lower = "기모바지"
        elif temperature > 8 and temperature <= 11:
            lower = "기모바지"
        elif temperature > 11 and temperature <= 16:
            lower = "청바지, 스타킹"
        elif temperature > 16 and temperature <= 19:
            lower = "긴바지"
        elif temperature > 19 and temperature <= 22:
            lower = "면바지, 슬렉스"
        elif temperature > 22 and temperature <= 27:
            lower = "반바지, 면바지"
        elif temperature > 28 and temperature <= 50:
            lower = "반바지, 짧은 치마"
        else:
            lower = "Unknown"
        
        data = {"temperature": temperature, "outer": outer, "upper":upper, "lower":lower}
        
        return Response(data)
    except ValueError:
        return Response({"error": "Invalid temperature value"}, status=400)