from django.urls import path
from .views import *
from . import views

app_name = "nalssi"
urlpatterns = [
    path('api/temperature/<path:temperature>/', views.temperature_grade),
]