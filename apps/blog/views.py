from django.shortcuts import render, redirect
from django.http import response, JsonResponse, HttpResponseRedirect
from .models import Article, Classfiy, Comment, Tag, Contatc
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page  # 导入缓存装饰器

# Create your views here.


# @cache_page(60 * 5)  # 缓存5分钟
def index(request, pindex):
    """显示首页视图"""
    Article_obj_list = Article.objects.get_article_list(sort='read')  # 获取文章列表
    classfiy_list = Classfiy.objects.get_all_classfiy()               # 获取分类列表
    tags = Tag.objects.get_list_object()                              # 获取标签列表
    # 分页
    if pindex == '':
        pindex = 1
    pindex = int(pindex)
    paginator = Paginator(Article_obj_list, 3)
    # 获取第pindex页内容
    Article_obj_list = paginator.page(pindex)  # 返回pindex页的page实例对象
    # 获取分页后的总数
    nums_pages = paginator.num_pages
    # 控制页码
    pindex = int(pindex)
    if nums_pages < 5:
        # 如果页面不足5页则全部显示
        pages = range(1, nums_pages + 1)
    elif pindex <= 3:
        # 当前页前三页，显示前五页
        pages = range(1, 6)
    elif nums_pages - pindex <= 2:  # 10 9 8 7
        # 当前页是后三页, 显示后五页
        pages = range(nums_pages - 4, nums_pages + 1)
    else:
        # 其他情况,显示当前页的前两页和后两页,当前页
        pages = range(pindex - 2, pindex + 3)
    New_Article_List = Article.objects.get_article_list(sort='new')[:4]      # 获取到最新4篇文章列表
    date_list = Article.objects.dates('create_time', 'month', order='DESC')  # 文章归档
    return render(request, 'blog/index.html', {'Article_obj_list': Article_obj_list,
                                               'Classfiy_List': classfiy_list,
                                               'tags': tags, 'pages': pages,
                                               'New_Article_List': New_Article_List,
                                               'date_list': date_list})


# @cache_page(60 * 5)  # 缓存15分钟
def about(request):
    """关于页面"""
    return render(request, 'blog/about.html')


# @cache_page(60 * 5)  # 缓存15分钟
def blog(request, article_id):
    """博客页面"""
    article = Article.objects.get_one_article(article_id=article_id)  # 通过文章id获取到文章
    article = Article.objects.get_html(article)          # 获取渲染成html的文本
    Article.objects.add_read_num(article_id=article_id)  # 增加文章的阅读量
    comment_list = Comment.objects.get_comment_list(article_id=article_id)     # 根据文章id获取文章所对应的评论
    New_Article_List = Article.objects.get_article_list(sort='new')  # 获取到最新的文章列表
    classfiy_list = Classfiy.objects.get_all_classfiy()  # 获取分类列表
    tags = Tag.objects.get_list_object()  # 获取标签列表
    date_list = Article.objects.dates('create_time', 'month', order='DESC')  # 文章归档
    return render(request, 'blog/detail.html', context={'article': article, 'comment_list': comment_list,
                                                        'New_Article_List': New_Article_List,
                                                        'Classfiy_List': classfiy_list,
                                                        'tags': tags, 'date_list': date_list})


def tidy(request, year, month):
    """根据归档查询显示"""
    article_list = Article.objects.get_article_list_by_month(year=year, month=month)
    return render(request, 'blog/temp.html', context={'article_list': article_list})


def classfiy(request, classfiy_id):
    """根据分类查询"""
    article_list = Article.objects.get_article_by_classfiy(classfiy_id=classfiy_id)  # 通过分类id获取到文章
    title = Classfiy.objects.get_classfiy(classfiy_id=classfiy_id).name
    return render(request, 'blog/temp.html', context={'article_list': article_list, 'title': title})


def tags(request, tags_id):
    """根据标签查询"""
    article_list = Article.objects.get_article_by_tags(tags_id=tags_id)  # 通过标签id获取到文章
    title = Tag.objects.get_tags(tags_id=tags_id).name
    return render(request, 'blog/temp.html', context={'article_list': article_list, 'title': title})


# @cache_page(60 * 5)  # 缓存5分钟
def Contact(request):
    """联系页面"""
    return render(request, 'blog/contact.html')


def contatc_post(request):
    """接收联系数据"""
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    Contatc.objects.create_contatc(name=name, email=email, subject=subject, message=message)
    return redirect('/')


def not_found(request):
    """404页面"""
    return render(request, 'error/404.html')


