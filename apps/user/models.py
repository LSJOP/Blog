from django.db import models
from apps.db.base_manager import BaseManager  # 导入抽象模型管理器基类
from apps.db.base_model import BaseModel


# Create your models here.


class PassportManager(BaseManager):
    """ 账户模型管理器类 """

    def add_one_passport(self, username, password, email):
        """添加用户注册信息"""
        obj = self.create_one_object(username=username, password=password, email=email)
        return obj

    def get_one_passport(self, username, password=None):
        """用户和密码校验"""
        if password is None:
            # 校验用户名是否重名
            obj = self.get_object(username=username)
            return obj
        else:
            # 登录校验
            obj = self.get_object(username=username, password=password)
            return obj


class Passport(BaseModel):
    """ 账户模型类 """
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(max_length=20, verbose_name='邮箱')

    objects = PassportManager()

    class Meta:
        db_table = 'blog_user_account'  # 指定表名
