from users.models import CarInfo, CarsImage, CarBrand, CarPriceInfo, IWantInfo
from xadmin import views
import xadmin


# Register your models here.
# 设置主题
class BaseThemSet(object):
    enable_themes = True
    use_bootswatch = True


# 设置标题
class CommSetting(object):
    site_title = 'XXX后台管理系统'
    site_footer = 'XXX网'
    # menu_style = 'accordion'


class CarInfoXadmin(object):
    list_display = ['user', 'title', 'area']

    # 添加附加选项表
    class ArtTagInlines(object):
        model = CarsImage
        style = 'tab'
        # exclude=['add_time']
        extra = 6

    inlines = [ArtTagInlines]


class CarsImageXadmin(object):
    list_display = ['car', 'image', ]


class CarBrandXadmin(object):
    list_display = ['name', ]
class CarPriceInfoXadmin(object):
    list_display = ['price', ]

class IWantInfoXadmin(object):
    list_display = ['name','mobile','brand','want_type','desc','address' ]


xadmin.site.register(IWantInfo, IWantInfoXadmin)
xadmin.site.register(CarPriceInfo, CarPriceInfoXadmin)

xadmin.site.register(CarInfo, CarInfoXadmin)
xadmin.site.register(CarBrand, CarBrandXadmin)
xadmin.site.register(CarsImage, CarsImageXadmin)
xadmin.site.register(views.BaseAdminView, BaseThemSet)
xadmin.site.register(views.CommAdminView, CommSetting)
