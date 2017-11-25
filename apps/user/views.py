from django.shortcuts import render, redirect
from apps.blog.models import Comment
from utils.decorators import login_required  # 判断登录装饰器
from .models import Passport
from .task import send_register_success_mail  # 导入发送邮件任务函数
from django.http import response, JsonResponse, HttpResponseRedirect
# Create your views here.


def login(request, num):
    """登录视图函数"""
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'user/index{}.html'.format(num))


def forgot(request, num):
    """忘记密码视图函数"""
    return render(request, 'user/forgot{}.html'.format(num))


def login_check(request):
    """用户登录验证"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 获取对象集合
    passport = Passport.objects.get_one_passport(username=username, password=password)
    if passport.exists():
        if 'pre_url_path' in request.session:
            # 返回用登录之前访问的地址
            pre_url_path = request.session['pre_url_path']
        else:
            pre_url_path = '/'
        # 使用session记录用户的登录状态
        request.session['islogin'] = True
        # 记录用户名
        request.session['username'] = username
        # 记录用户id
        request.session['passport'] = passport[0].id  # passport是个查询集,使用下标拿到对象,然后获取对象的id
        # 当密码和用户名正确时会返回True
        jres = JsonResponse({'res': 1, 'pre_url_path': pre_url_path})
        if remember:
            # 当记住用户名被选中
            jres.set_cookie('username', username, max_age=14 * 24 * 3600)
        return jres
    else:
        return JsonResponse({'res': 0})  # 密码或用户名错误


def logout(request):
    """退出登录"""
    # 清除session的登录状态
    request.session.flush()
    # 跳转到首页
    return redirect('/')


def register(request, num):
    """用户注册函数"""
    if request.method == 'GET':
        """显示注册页面"""
        return render(request, 'user/sign-up{}.html'.format(num))
    else:
        """处理用户注册信息"""
        username = request.POST.get('name')  # 获取用户名
        password = request.POST.get('password')  # 获取密码
        email = request.POST.get('email')   # 获取邮箱
        Passport.objects.add_one_passport(username, password, email)  # 将注册信息保存进数据库
        send_register_success_mail.delay(username=username, email=email)  # 发送注册成功邮件
        return redirect('/user/index/')  # 跳转至登录页面


def check_user_exist(request):
    """用户名验证"""
    username = request.POST.get('username')
    if Passport.objects.get_one_passport(username=username).exists():
        res = 1
    else:
        res = 0
    return JsonResponse({'res': res})


@login_required
def comment(request, article_id):
    """接收用户评论"""
    name = request.POST.get('name')
    email = request.POST.get('email')
    url = request.POST.get('url')
    comment = request.POST.get('comment')
    addr = '中国大陆'
    article_id = int(article_id)
    Comment.objects.create_comment_by_article(name=name, email=email, comment=comment, addr=addr, article_id=article_id)
    return redirect('/')

@login_required
def user(request):
    """个人信息页"""
    username = request.session.get('username')     # 获取用户名
    passport_id = request.session.get('passport')  # 获取用户id
    # obj = Address.objects.get_recipient_address(passport_id=passport_id)
    return render(request, 'build/build.html')

