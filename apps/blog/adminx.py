import xadmin
from .models import Article, Tag, Classfiy, Comment


class ArticleAdmin(object):
    """文章模型管理类"""
    list_display = ['title', 'tags', 'author', 'classfiy']


class TagAdmin(object):
    """标签模型管理类"""
    list_display = ['name']


class ClassfiyAdmin(object):
    """分类模型管理类"""
    list_display = ['name']


class CommentAdmin(object):
    """评论模型管理类"""
    list_display = ['name', 'addr']


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Classfiy, ClassfiyAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)


