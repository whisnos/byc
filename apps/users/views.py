from django.db.models import Q
from django.shortcuts import render, HttpResponse

# Create your views here.
from users.models import CarBrand, CarPriceInfo, CarInfo


def index(request):
    return render(request, 'index.html')


def buy_car(request):
    all_brands = CarBrand.objects.all()
    all_car_prices = CarPriceInfo.objects.all()
    choice_areas = {
        '思明区': '思明区',
        '湖里区': '湖里区',
        '集美区': '集美区',
        '杏林区': '杏林区',
        '海沧区': '海沧区',
        '翔安区': '翔安区',
        '芗城区': '芗城区',
        '龙文区': '龙文区',
    }
    return render(request, 'buy_car.html', {
        'all_brands': all_brands,
        'all_car_prices': all_car_prices,
        'choice_areas': choice_areas,
    })


def test(request):
    print('test......................')
    print('request.GET', request.GET)
    pp = request.GET.get('arr[pp]', '')  # 品牌
    yls = request.GET.get('arr[yls]', '')  # 价格
    zz = request.GET.get('arr[zz]', '')  # 车龄
    guishudi = request.GET.get('arr[guishudi]', '')  # 归属地
    fy = request.GET.get('arr[fy]', '')  # 分页
    print('品牌', pp)
    filter = Q()
    if pp:
        print(22)
        filter = Q(car_brand=pp)

    if yls:
        yls = yls.replace('万', '')
        yls = yls.split('-')
        l_price = yls[0]
        g_price = yls[1]
        print('yls', l_price, g_price)
        if not pp:
            filter = Q(car_price__gte=int(l_price)) & Q(car_price__lte=int(g_price))
        else:
            filter = Q(car_brand=pp) & Q(car_price__gte=int(l_price)) & Q(car_price__lte=int(g_price))
    if zz:
        print(22)
        filter = Q(car_brand=pp)
    if pp:
        print(22)
        filter = Q(car_brand=pp)
    print('filter', filter)
    all_cars = CarInfo.objects.filter(filter)
    print('all_cars', all_cars)
    if not all_cars:
        all_cars = ''
    return render(request, 'car_info.html', {
        'all_cars': all_cars,
    })
