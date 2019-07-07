"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

import schoolteam
from DjangoServer import settings
from schoolteam import views

import  xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^chat/', include('schoolteam.urls')),
    # url(r'^admin/', admin.site.urls),
    #web
    url('web_index/', views.web_index),
    url('test/', views.test),
    url('web_admin/', views.web_admin),
    url('web_login/', views.web_login),
    path('web_register/', views.web_register),
    url('logout/', views.logout_web),
    # json
    path('judge_login/', views.judge_login),
    path('search/', views.search),
    path('login/', views.login),
    path('release_team/', views.release_team),
    path('get_data/', views.get_data),
    path('update/', views.update),
    path('get_team/', views.get_team),
    path('sign_up/', views.sign_up),
    path('get_team_by_category/', views.get_team_by_category),
    path('show_recommend/', views.show_recommend),
    path('get_message/', views.get_message),
    path('get_myteam/', views.get_myteam),
    path('join_team/', views.join_team),
    path('get_name_by_id/', views.get_name_by_id),
    path('update_avator/', views.updata_avator),

    # re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]