from django.contrib import admin

# Register your models here.
from schoolteam.models import Team, RecommendContest, Users, Message
import xadmin
from xadmin import views
# admin.site.register(Users)
# admin.site.register(Team)
# admin.site.register(Message)
# admin.site.register(RecommendContest)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '校队后台管理系统'
    site_footer = 'schoolteam.com'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Users)
xadmin.site.register(Team)
xadmin.site.register(Message)
xadmin.site.register(RecommendContest)
