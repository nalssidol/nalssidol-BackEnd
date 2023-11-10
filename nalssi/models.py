from django.db import models

# Create your models here.

# 날씨 모델
class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    # 외투
    outer = models.CharField(max_length=50)
    # 상의
    top = models.CharField(max_length=50)
    # 하의
    pants = models.CharField(max_length=50)
    # 돌돌이 이미지
    dol = models.ImageField(upload_to='weather_images/', null=True, blank=True)