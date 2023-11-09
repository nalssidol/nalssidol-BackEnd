from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from .serializers import *

import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

def get_nxny(city_name, gu_name):
    df = pd.read_excel("static/weather.xlsx")

    result = df[(df['1단계'] == city_name) & (df['2단계'] == gu_name)]
    if not result.empty:
        return result.iloc[0]['격자 X'], result.iloc[0]['격자 Y']
    else:
        return None, None

@api_view(['GET'])
def location_data(request):
    city_name = request.query_params.get('city', None)
    gu_name = request.query_params.get('gu', None)
    
    if city_name is not None and gu_name is not None:
        nx, ny = get_nxny(city_name, gu_name)
        if nx is not None and ny is not None:
            return Response({'city': city_name, 'gu': gu_name,'nx': nx, 'ny': ny})
        else:
            return Response({'error': '데이터가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': '시와 구를 입력해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
