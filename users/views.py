from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Saunas, Category

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def popular_list(request):
    saunas = Saunas.objects.filter(available=True)[:3]
    return  render(request,
                   "users/index/index.html",
                   {'saunas':saunas})

def sauna_detail(request,slug):
    sauna = get_object_or_404(Saunas,
                               slug=slug,
                               available=True)
    return render(request,
                  'users/sauna/detail.html',
                  {'sauna': sauna}),

