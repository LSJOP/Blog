from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^about/$', view=about),         # 关于页面
    url(r'^blog/(\d+)/$', view=blog),     # 博客页面
    url(r'^contact/$', view=Contact),     # 联系页面
    url(r'^comment/$', view=Comment),     # 用户评论
    url(r'^$', view=index),               # 显示博客首页
    url(r'/', view=not_found),            # 404页面
]
