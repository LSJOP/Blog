from django.conf.urls import url
from .views import login, forgot, login_check, logout, register, check_user_exist, comment


urlpatterns = [
    url(r'index/(\d*)', view=login),           # 登录页面
    url(r'forgot/(\d*)', view=forgot),         # 忘记密码
    url(r'sign-up/(\d*)', view=register),       # 注册
    url(r'^comment/(\d+)', view=comment),      # 用户评论
    url(r'^login_check/$', view=login_check),  # 用户登录验证
    url(r'^logout/$', view=logout),            # 退出登录
    url(r'^register/(\d*)', view=register),        # 用户注册视图
    url(r'^register_check/$', view=check_user_exist),  # 验证用户名是否存在
]
