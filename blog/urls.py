from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
	(r'^$','archive'),
	(r'^create/','create_blogpost'),
	)