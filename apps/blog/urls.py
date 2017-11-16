from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^about/$', view=about),         # 关于页面
    url(r'^blog/(\d+)/$', view=blog),     # 博客页面
    url(r'^contact/$', view=Contact),     # 联系页面
    url(r'^tags/(\d+)$', view=tags),      # 根据标签查询
    url(r'^classfiy/(\d+)', view=classfiy),   # 根据分类显示
    url(r'^tidy/(?P<year>[\d+]{4})/(?P<month>[\d+]{1,2})', view=tidy),  # 根据归档显示
    url(r'^contatc_post/$', view=contatc_post),  # 接收联系的数据
    url('(?P<pindex>\d*)|[/]', view=index),   # 显示博客首页
    url(r'\w+', view=not_found),              # 404页面
]
