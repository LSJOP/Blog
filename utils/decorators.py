from django.shortcuts import  redirect


def login_required(view_func):
    """登录判断装饰器"""
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('islogin'):
            # 已登录
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 未登录
            return redirect('/user/login/')
    return wrapper
