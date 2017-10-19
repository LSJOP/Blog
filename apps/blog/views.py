from django.shortcuts import render
from django.http import response
# Create your views here.


def index(request):
    """显示首页视图"""
    return render(request, 'index.html')


def login(request):
    """联系页面"""
    pass


def about(request):
    """关于页面"""
    pass


def blog(request):
    """博客页面"""
    pass


