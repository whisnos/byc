from django.shortcuts import render


# Create your views here.
from users.models import CarBrand, CarPriceInfo


def index(request):
    return render(request, 'index.html')


def buy_car(request):
    all_brands=CarBrand.objects.all()
    all_car_prices=CarPriceInfo.objects.all()
    return render(request, 'buy_car.html',{
        'all_brands':all_brands,
        'all_car_prices':all_car_prices,
    })
