from .db.base_manager import BaseManager
from .db.base_model import BaseModel
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ClassfiyManager(BaseManager):
    """分类模型管理器类"""

    def get_all_classfiy(self, ):
        """获取所有文章分类"""
        classfiy_obj = self.all()
        if classfiy_obj.exists():
            return classfiy_obj
        else:
            return None


class Classfiy(BaseModel):
    """文章分类模型"""
    name = models.CharField(max_length=20, verbose_name='标签')

    objects = ClassfiyManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
        db_table = 'blog_classfiy'


class TagManager(BaseManager):
    """标签模型管理器类"""
    pass


class Tag(BaseModel):
    """文章标签模型"""
    name = models.CharField(max_length=30, verbose_name='标签')

    objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name
        db_table = 'blog_tag'


class ArticleManager(BaseManager):
    """文章模型管理器类"""

    def get_one_article(self, article_id):
        """获取一篇文章"""
        article_obj = self.get_object(id=article_id)
        if article_obj.exists():
            return article_obj[0]
        else:
            return None

    def get_list_article(self):
        """获取文章集合"""
        article_list = self.get_list_object(filters={}, order_by=('-read_num',))  # 根据文章阅读量进行排序
        if article_list.exists():
            return article_list
        else:
            return None


class Article(BaseModel):
    """文章模型"""
    title = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    author = models.ForeignKey(User, verbose_name='作者')
    classfiy = models.ForeignKey(Classfiy, verbose_name='分类')
    read_num = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = 'blog_article'


class CommentManager(BaseManager):
    """评论模型管理器类"""

    def get_comment_list(self, article_id):
        """获取评论"""
        comment_list = self.get_list_object(filters={'article_id': article_id}, order_by=('-update_time',))  # 获取最新评论
        if comment_list.exists():
            return comment_list
        else:
            return None


class Comment(BaseModel):
    """评论模型类"""
    comment = models.CharField(max_length=1024, verbose_name='评论')
    name = models.CharField(max_length=30, verbose_name='名字')
    email = models.EmailField(max_length=20, verbose_name='邮箱')
    addr = models.CharField(max_length=40, verbose_name='用户发表评论时的地址')
    article = models.ForeignKey(Article, verbose_name='所属文章')

    objects = CommentManager()

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 'blog_comment'


