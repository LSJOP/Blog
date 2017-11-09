from django.shortcuts import render, redirect


class UrlPathRecordMiddleware(object):
    """记录用户访问地址中间间类"""
    exclude_path = ['/user/login/', '/user/register/', '/user/logout/']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """记录用户访问地址"""
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']


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
