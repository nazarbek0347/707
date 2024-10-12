from django.contrib import admin
from django.urls import path,include
from .views import taomlar,ichimliklar

urlpatterns = [
    path('',taomlar,name='taomlarPage'),
    path('ichimliklar',ichimliklar,name='ichimliklarPage')
]
