from zoneinfo import available_timezones

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from unicodedata import category

from .models import Saunas, Category


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def popular_list(request):
    saunas = Saunas.objects.filter(available=True)[:3]
    return  render(request,
                   "users/index/index.html",
                   {'saunas':saunas})


def sauna_detail(request, slug):
    sauna = Saunas.objects.filter(slug=slug, available=True).first()

    if sauna is None:
        raise Http404("Sauna not found")  # Вместо None — 404

    return render(request, 'users/sauna/detail.html', {'sauna': sauna})

def saunas_list(request, category_slug=None):
    page = request.GET.get('page',1)
    category = None
    categories = Category.objects.all()
    saunas = Saunas.objects.filter(available=True)
    paginator = Paginator(saunas,10)
    current_page=paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        paginator=Paginator(saunas.filter(category=category),10)
        current_page = paginator.page(int(page))
    return render(request,
                  'users/sauna/list.html',
                  {'category':category,
                            'categories':categories,
                            'saunas':current_page,
                            'slug_url': category_slug},)








