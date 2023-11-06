from django.urls import path
from .views import *

urlpatterns = [
    path('location/', location_data),
]
