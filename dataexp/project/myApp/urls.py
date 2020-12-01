from django.conf.urls import url
from django.views.generic import TemplateView

from . import views #.代表当前目录
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.index1),
    url(r'^index/$', views.index),

    #到达注册页面
    url(r'^to_register/$', views.to_register),
    #注册页面完成注册
    url(r'^register/$', views.register),

    #登录
    url(r'^to_login/$', views.to_login),
    url(r'^login/$', views.login),

    #数据集选择页面
    url(r'^to_dataset/$', views.to_dataset),

    #数据属性选择页面
    url(r'^to_dataAttr/$', views.to_dataAttr),

    #数据反馈页面
    url(r'^to_feedback/$', views.to_feedback),

    #数据反馈
    url(r'^dataFeedback/$', views.dataFeedback),

    #退出登录
    url(r'^quit/$', views.quit),
]
