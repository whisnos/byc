from django.shortcuts import render


# Create your views here.
from users.models import CarBrand, CarPriceInfo


def index(request):
    return render(request, 'index.html')


def buy_car(request):
    all_brands=CarBrand.objects.all()
    all_car_prices=CarPriceInfo.objects.all()
    choice_areas = {
        0:'思明区',
        1:'湖里区',
        2:'集美区',
        3:'杏林区',
        4:'海沧区',
        5:'翔安区',
        6:'芗城区',
        7:'龙文区',
    }
    return render(request, 'buy_car.html',{
        'all_brands':all_brands,
        'all_car_prices':all_car_prices,
        'choice_areas':choice_areas,
    })
