from django.shortcuts import render
from django.http import response, JsonResponse, HttpResponseRedirect
# Create your views here.


def login(request, num):
    """登录视图函数"""

    return render(request, 'login/index{}.html'.format(num))


def forgot(request, num):
    """忘记密码视图函数"""

    return render(request, 'login/forgot{}.html'.format(num))


def sign_up(request, num):
    """注册视图函数"""

    return render(request, 'login/sign-up{}.html'.format(num))
