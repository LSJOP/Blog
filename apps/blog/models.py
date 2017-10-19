from .db.base_manager import BaseManager
from .db.base_model import BaseModel
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ClassfiyManager(BaseManager):
    """分类模型管理器类"""
    pass


class Classfiy(BaseModel):
    """文章分类模型"""
    name = models.CharField(max_length=20, verbose_name='标签')

    objects = ClassfiyManager()

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

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name
        db_table = 'blog_tag'


class ArticleManager(BaseManager):
    """文章模型管理器类"""
    pass


class Article(BaseModel):
    """文章模型"""
    title = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    author = models.ForeignKey(User, verbose_name='作者')
    classfiy = models.ForeignKey(Classfiy, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签', db_table='Article_to_Tag')
    objects = ArticleManager()

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = 'blog_article'



