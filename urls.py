#-*-coding:utf-8-*-
from django.conf.urls.defaults import *

#Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#patterns()函数接收两个元组（URL 正则表达式,目标)
urlpatterns = patterns('',
    # Example:
     (r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
