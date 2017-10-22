from django.shortcuts import render
from django.http import response
from .models import Article, Classfiy, Comment, Tag


# Create your views here.


def index(request, pindex):
    """显示首页视图"""
    Article_obj_list = Article.objects.get_article_list(sort='read')  # 获取文章列表
    classfiy_list = Classfiy.objects.get_all_classfiy()          # 获取分类列表
    tags = Tag.objects.get_list_object()                    # 获取标签列表
    for article in Article_obj_list:
        article.comment_num = article.comment_set.count     # 增加评论数量属性
    pages, Article_obj_list = Article.objects.get_page(pindex=pindex, Article_obj_list=Article_obj_list)
    New_Article_List = Article.objects.get_article_list(sort='new')  # 获取到最新的文章列表
    return render(request, 'blog/index.html', {'Article_obj_list': Article_obj_list, 'Classfiy_List': classfiy_list,
                                               'tags': tags, 'pages': pages, 'New_Article_List': New_Article_List})


def about(request):
    """关于页面"""
    return render(request, 'blog/about.html')


def blog(request, article_id):
    """博客页面"""
    article = Article.objects.get_one_article(article_id=article_id)  # 通过文章id获取到文章
    article = Article.objects.get_html(article)      # 获取渲染成html的文本
    article.comment_num = article.comment_set.count  # 增加评论数量属性
    Article.objects.add_read_num(article_id=article_id)  # 增加文章的阅读量
    comment_list = Comment.objects.get_comment_list(article_id=article_id)     # 根据文章id获取文章所对应的评论
    New_Article_List = Article.objects.get_article_list(sort='new')  # 获取到最新的文章列表
    classfiy_list = Classfiy.objects.get_all_classfiy()  # 获取分类列表
    tags = Tag.objects.get_list_object()  # 获取标签列表

    return render(request, 'blog/detail.html', context={'article': article, 'comment_list': comment_list,
                                                        'New_Article_List': New_Article_List, 'Classfiy_List': classfiy_list,
                                                        'tags': tags})


def tidy(request, year, month):
    """根据归档查询显示"""
    pass


def classfiy(request, classfiy):
    """根据分类查询"""
    pass


def tags(request, tags):
    """根据标签查询"""
    pass


def Contact(request):
    """联系页面"""
    return render(request, 'blog/contact.html')


def comment(request):
    """接收用户评论"""
    pass


def not_found(request):
    """404页面"""
    return render(request, 'error/404.html')


