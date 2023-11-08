from .models import Weather
from .serializers import WeatherSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView

from django.http import FileResponse, JsonResponse
from django.conf import settings

import os
import base64

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
            top = "니트, 맨투맨, 후드"
        elif temperature > 4 and temperature <= 8:
            top = "니트, 맨투맨, 후드"
        elif temperature > 8 and temperature <= 11:
            top = "니트, 맨투맨, 후드"
        elif temperature > 11 and temperature <= 16:
            top = "니트, 맨투맨, 후드"
        elif temperature > 16 and temperature <= 19:
            top = "니트, 맨투맨, 후드"
        elif temperature > 19 and temperature <= 22:
            top = "블라우스, 긴팔 티"
        elif temperature > 22 and temperature <= 27:
            top = "반팔, 얇은 셔츠"
        elif temperature > 28 and temperature <= 50:
            top = "민소매, 반팔"
        else:
            top = "Unknown"

        # 하의 추천
        if temperature >= -30 and temperature <= 4:
            pants = "기모바지"
        elif temperature > 4 and temperature <= 8:
            pants = "기모바지"
        elif temperature > 8 and temperature <= 11:
            pants = "기모바지"
        elif temperature > 11 and temperature <= 16:
            pants = "청바지, 스타킹"
        elif temperature > 16 and temperature <= 19:
            pants = "긴바지"
        elif temperature > 19 and temperature <= 22:
            pants = "면바지, 슬렉스"
        elif temperature > 22 and temperature <= 27:
            pants = "반바지, 면바지"
        elif temperature > 28 and temperature <= 50:
            pants = "반바지, 짧은 치마"
        else:
            pants = "Unknown"
        
        # 온도에 따른 돌 사진 불러오기
        image_name = None
        if temperature >= -30 and temperature <= 4:
            image_name = "5.png"
        elif temperature > 4 and temperature <= 8:
            image_name = "6.png"
        elif temperature > 8 and temperature <= 11:
            image_name = "10.png"
        elif temperature > 11 and temperature <= 16:
            image_name = "12.png"
        elif temperature > 16 and temperature <= 19:
            image_name = "17.png"
        elif temperature > 19 and temperature <= 22:
            image_name = "20.png"
        elif temperature > 22 and temperature <= 27:
            image_name = "23.png"
        elif temperature > 28 and temperature <= 50:
            image_name = "28.png"
        else:
            dol = "Unknown"

        data = {
            "temperature": temperature,
            "outer": outer,
            "top": top,
            "pants": pants,
        }

        if image_name:
            image_url = request.build_absolute_uri(f'{settings.STATIC_URL}img/{image_name}')
            data["dol"] = image_url
        else:
            data["dol"] = "No image available for this temperature range"

        return Response(data)


    except ValueError:
        return Response({"error": "Invalid temperature value"}, status=400)