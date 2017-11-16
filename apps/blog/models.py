from apps.db.base_manager import BaseManager
from apps.db.base_model import BaseModel
import markdown
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


# Create your models here.


class ClassfiyManager(BaseManager):
    """分类模型管理器类"""

    def get_all_classfiy(self):
        """获取所有文章分类"""
        classfiy_obj_list = self.all()
        if classfiy_obj_list.exists():
            for classfiy_obj in classfiy_obj_list:
                # 给分类增加数量属性
                classfiy_obj.sum = classfiy_obj.article_set.all().filter(classfiy=classfiy_obj.id).count()
            return classfiy_obj_list
        else:
            return None

    def get_classfiy(self, classfiy_id):
        """获取到分类对象"""
        classfiy_obj = self.get_object(id=classfiy_id)
        if classfiy_obj.exists():
            return classfiy_obj[0]
        else:
            return None


class Classfiy(BaseModel):
    """文章分类模型"""
    name = models.CharField(max_length=20, verbose_name='文章分类')

    objects = ClassfiyManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
        db_table = 'blog_classfiy'


class TagManager(BaseManager):
    """标签模型管理器类"""

    def get_tag_list(self):
        """获取标签列表"""
        tag_obj_list = self.get_list_object()
        if tag_obj_list.exists():
            return tag_obj_list
        else:
            return None

    def get_tags(self, tags_id):
        """获取到分类对象"""
        tag_obj = self.get_object(id=tags_id)
        if tag_obj.exists():
            return tag_obj[0]
        else:
            return None


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
            article_obj = article_obj[0]
            article_obj.comment_num = article_obj.comment_set.count  # 增加评论数量属性
            return article_obj
        else:
            return None

    def get_article_list(self, sort='read'):
        """获取文章集合"""
        if sort == 'read':
            sort = ('-read_num',)         # 根据文章阅读量进行排序
        elif sort == 'new':
            sort = ('update_time',)       # 根据文章更新时间进行排序
        article_list = self.get_list_object(filters={}, order_by=sort)
        if article_list.exists():
            for article_obj in article_list:
                article_obj.comment_num = article_obj.comment_set.count  # 增加评论数量属性
            return article_list
        else:
            return None

    def get_html(self, article):
        """得到渲染后的文本"""
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            TocExtension(slugify=slugify),     # 自动生成目录
        ])
        article.body = md.convert(article.body)  # 将文章渲染成html格式
        article.toc = md.toc  # 文章目录
        return article

    def add_read_num(self, article_id):
        """增加文章阅读量"""
        article_obj = self.get_one_article(article_id=article_id)  # 根据文章id获取到文章
        article_obj.read_num = int(article_obj.read_num) + int(1)
        article_obj.save()

    def get_article_list_by_month(self, year, month):
        """根据月份获取文章集合"""
        article_list = self.get_article_list()  # 获取文章集合
        article_list = article_list.filter(create_time__year=year, create_time__month=month)
        if article_list.exists():
            for article_obj in article_list:
                article_obj.comment_num = article_obj.comment_set.count  # 增加评论数量属性
            return article_list
        else:
            return None

    def get_article_by_tags(self, tags_id):
        """根据标签id或分类id获取文章"""
        article_obj_list = self.get_list_object(filters={'tags': tags_id})
        if article_obj_list.exists():
            for article_obj in article_obj_list:
                article_obj.comment_num = article_obj.comment_set.count  # 增加评论数量属性
            return article_obj_list
        else:
            return None

    def get_article_by_classfiy(self, classfiy_id):
        """根据标签获取文章"""
        article_obj_list = self.get_list_object(filters={'classfiy': classfiy_id})
        if article_obj_list.exists():
            for article_obj in article_obj_list:
                article_obj.comment_num = article_obj.comment_set.count  # 增加评论数量属性
            return article_obj_list
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

    def create_comment_by_article(self, comment, name, email, addr, article_id):
        """根据文章id添加评论"""
        self.create_one_object(comment=comment, name=name, email=email, addr=addr, article_id=article_id)
        print('create ')


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


class ContatcManager(BaseManager):
    """联系模型管理器类"""

    def create_contatc(self, name, subject, email, message):
        """保存联系"""
        self.create_one_object(name=name, subject=subject, email=email, message=message)


class Contatc(BaseModel):
    """联系模型类"""
    name = models.CharField(max_length=30, verbose_name='姓名')
    subject = models.CharField(max_length=60, verbose_name='主题')
    email = models.EmailField(max_length=20, verbose_name='邮箱')
    message = models.TextField(verbose_name='内容')

    objects = ContatcManager()

    def __str__(self):
        return self.Contatc

    class Meta:
        verbose_name = '联系'
        verbose_name_plural = verbose_name
        db_table = 'blog_Contatc'

