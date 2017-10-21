from django.shortcuts import render
from django.http import response
from .models import Article, Classfiy, Comment
import markdown
# Create your views here.


def index(request):
    """显示首页视图"""
    Article_obj_list = Article.objects.get_list_article()  # 获取文章列表
    classfiy = Classfiy.objects.get_list_object()          # 获取分类列表
    for article in Article_obj_list:
        tags = article.tags
        article.comment_num = article.comment_set.count    # 增加评论数量属性
    return render(request, 'blog/index.html', {'Article_obj_list': Article_obj_list, 'Classfiy': classfiy})


def about(request):
    """关于页面"""
    return render(request, 'blog/about.html')


def blog(request, article_id):
    """博客页面"""
    article = Article.objects.get_one_article(article_id=article_id)  # 通过文章id获取到文章
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',  # 语法高亮拓展
                                      'markdown.extensions.toc',         # 自动生成目录
                                  ])
    article.comment_num = article.comment_set.count  # 增加评论数量属性
    comment = Comment.objects.get_comment_list(article_id=article_id)     # 根据文章id获取文章所对应的评论
    return render(request, 'blog/detail.html', context={'article': article, 'comment': comment})


def Contact(request):
    """联系页面"""
    return render(request, 'blog/contact.html')


def comment(request):
    """接收用户评论"""
    pass


def not_found(request):
    """404页面"""
    return render(request, 'error/404.html')


