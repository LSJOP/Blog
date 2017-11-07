from django.conf.urls import url
from .views import login, forgot, sign_up


urlpatterns = [
    url(r'index/(\d*)', view=login),         # 登录页面
    url(r'forgot/(\d*)', view=forgot),       # 忘记密码
    url(r'sign-up/(\d*)', view=sign_up),     # 登录
]
