from .db.base_manager import BaseManager
from .db.base_model import BaseModel
from django.db import models
from django.contrib.auth.models import User
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.core.paginator import Paginator
from django.db.models import Sum
# Create your models here.


class ClassfiyManager(BaseManager):
    """分类模型管理器类"""

    def get_all_classfiy(self, ):
        """获取所有文章分类"""
        classfiy_obj_list = self.all()
        if classfiy_obj_list.exists():
            for classfiy_obj in classfiy_obj_list:
                # 给分类增加数量属性
                classfiy_obj.sum = classfiy_obj.article_set.all().aggregate(Sum('classfiy_id'))['classfiy_id__sum']  # 拿到的是一个字典,name__sum是键
            return classfiy_obj_list
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

    def get_tag_list(self):
        """获取标签列表"""
        tag_obj_list = self.get_list_object()
        if tag_obj_list.exists():
            return tag_obj_list
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
            return article_obj[0]
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
            return article_list
        else:
            return None

    def get_html(self, article):
        """得到渲染后的文本"""
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            TocExtension(slugify=slugify),  # 自动生成目录
        ])
        article.body = md.convert(article.body)  # 将文章渲染成html格式
        article.toc = md.toc  # 文章目录
        return article

    def get_page(self, pindex, Article_obj_list):
        """将博客进行分页"""
        if type(pindex) is str:
            pindex = 1
        # 分页
        paginator = Paginator(Article_obj_list, 4)
        # 获取第pindex页内容
        Article_obj_list = paginator.page(int(pindex))  # 返回pindex页的page实例对象
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
        return pages, Article_obj_list

    def add_read_num(self, article_id):
        """增加文章阅读量"""
        article_obj = self.get_one_article(article_id=article_id)  # 根据文章id获取到文章
        article_obj.read_num = int(article_obj.read_num) + int(1)
        article_obj.save()

    def get_article_list_by_month(self, year, month):
        """根据月份获取文章集合"""
        article_list = self.get_article_list()  # 获取文章集合
        article_list = article_list.filter(pub_date__year=year, pub_date__month=month)
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


