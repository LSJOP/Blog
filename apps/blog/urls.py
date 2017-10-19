from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'', view=index)  # 显示博客首页
]
