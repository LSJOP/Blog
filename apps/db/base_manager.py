from django.db import models
import copy


class BaseManager(models.Manager):
    """模型管理器基类"""

    def get_all_valid_fields(self):
        """获取self所在模型类的有效属性"""
        attr_str_list = []
        models_class = self.model
        attr_tuple = models_class._meta.get_fields()
        for attr in attr_tuple:
            if isinstance(attr, models.ForeignKey):
                attr_name = '%s_id' % attr.name
            else:
                attr_name = attr.name
            attr_str_list.append(attr_name)
        return attr_str_list

    def get_object(self, **filters):
        """获取一个查询集"""
        obj = self.filter(**filters)
        return obj

    def create_one_object(self, **kwargs):
        """新增self所在模型类数据"""
        valid_fields = self.get_all_valid_fields()
        kws = copy.copy(kwargs)
        # 去除valid_fields中的无效参数
        for key in kws:
            if key not in valid_fields:
                valid_fields.pop(key)
        obj = self.model(**kwargs)
        obj.save()
        return obj

    def get_list_object(self, filters={}, order_by=('-pk',)):
        """按照filters中的条件查询数据，进行排序"""
        object_list = self.filter(**filters).order_by(*order_by)
        return object_list
