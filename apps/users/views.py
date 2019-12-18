from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from byc.settings import PAGE_SIZE, DISPLAY
from users.helper import iPagination
from users.models import CarBrand, CarPriceInfo, CarInfo, IWantInfo


def index(request):
    chao_di=CarInfo.objects.filter(car_type=4).order_by('add_time')[:6]
    re_men=CarInfo.objects.filter(car_type=3).order_by('add_time')[:6]
    jing_ji=CarInfo.objects.filter(car_type=2).order_by('add_time')[:6]
    super_suv=CarInfo.objects.filter(car_type=1).order_by('add_time')[:6]
    mian_bao=CarInfo.objects.filter(car_type=0).order_by('add_time')[:6]
    return render(request, 'index.html',{
        "chao_di":chao_di,
        "re_men":re_men,
        "jing_ji":jing_ji,
        "super_suv":super_suv,
        "mian_bao":mian_bao


    })


def buy_car(request):
    pf=request.GET.get('pf','')
    the_type_on=False
    if pf in['0','1','2','3','4']:
        the_type_on=pf
    all_brands = CarBrand.objects.all()
    all_car_prices = CarPriceInfo.objects.all()
    if pf:
        all_car_prices.filter()
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
        'the_type_on':the_type_on
    })


def test(request):
    print('test......................')
    print('request.GET', request.GET)
    pp = request.GET.get('arr[pp]', '')  # 品牌
    yls = request.GET.get('arr[yls]', '')  # 价格
    zz = request.GET.get('arr[zz]', '')  # 车龄
    guishudi = request.GET.get('arr[guishudi]', '')  # 归属地
    pf = request.GET.get('arr[pf]', '')  # 类型
    fy = request.GET.get('arr[fy]', 1)  # 分页
    if fy:
        try:
            page=int(fy)
            offset = (page - 1) * PAGE_SIZE
        except:
            offset=0


    print('品牌', pp)
    yls1 = Q()
    if pp:
        print(22)
        pp1 = Q(car_brand=pp)
    else:
        pp1 = Q()
    if yls:
        yls = yls.replace('万', '')
        yls = yls.split('-')
        l_price = yls[0]
        g_price = yls[1]
        print('yls', l_price, g_price)
        # if not pp:
        #     yls1 = Q(car_price__gte=int(l_price)) & Q(car_price__lte=int(g_price))
        # else:
        #     yls1 = pp1 & Q(car_price__gte=int(l_price)) & Q(car_price__lte=int(g_price))
        yls1 = pp1 & Q(car_price__gte=int(l_price)) & Q(car_price__lte=int(g_price))
    else:
        yls1 = pp1
    if zz:
        zz = zz.split('-')
        l_age = zz[0]
        g_age = zz[1]
        print('zz', l_age, g_age)
        yls1 = Q(car_age__gte=int(l_age)) & Q(car_age__lte=int(g_age)) & yls1
    else:
        yls1 = yls1
    if guishudi:

        yls1 = Q(area=int(guishudi)) & yls1
    else:
        yls1 =  yls1
    if pf:
        yls1 = yls1 & Q(car_type=int(pf))
    else:
        yls1 = yls1

    all_cars = CarInfo.objects.filter(yls1)[offset:offset+PAGE_SIZE:]
    page_params = {
        'total': all_cars.count(),
        'page_size': PAGE_SIZE,
        'page': int(fy),
        'display': DISPLAY,
        'url': request.path.replace('&p={}'.format(int(fy)), '?')
    }
    pages = iPagination(page_params)
    print('all_cars', all_cars)
    if not all_cars:
        all_cars = ''
    return render(request, 'car_info.html', {
        'all_cars': all_cars,
        'pages':pages
    })
def user_buy_car(request):
    if request.method == 'POST':
        print('request.POST', request.POST)
        data={}
        data['name'] = request.POST.get('name', '')  # 姓名
        data['mobile'] = request.POST.get('num', '')  # 电话
        data['brand'] = request.POST.get('car', '')  # 品牌
        data['desc'] = request.POST.get('xuqiu', '')  # 描述
        data['address'] = request.POST.get('addr', '')  # 地址
        want_type = request.POST.get('type', '')  # 品牌
        if want_type == '0':
            data['want_type']=0
            IWantInfo.objects.create(**data)
        else:
            data['want_type'] = 1
            IWantInfo.objects.create(**data)
    else:
        pass
    return HttpResponse('ok')