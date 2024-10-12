from django.shortcuts import render
from .models import Taomlar, Ichimliklar
# Create your views here.

def taomlar(request):
    taomlar=Taomlar.objects.all()
    return render(request,'taomlar.html', {"taomlar":taomlar})

def ichimliklar(request):
    ichimliklar = Ichimliklar.objects.all()
    return render(request, 'ichimliklar.html', {'ichimliklar': ichimliklar})