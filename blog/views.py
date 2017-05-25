#-*-coding:utf-8-*-
# Create your views here.
from blog.models import BlogPost,BlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.views.generic.simple import direct_to_template

#精简为单行代码 archive = lambda req:render_to_response('archive.html',{'posts':BlogPost.objects.all()[:10]})
def archive(request):
	posts = BlogPost.objects.all() [:10]
	return direct_to_template(request,'archive.html',{'posts':posts,
		'form':BlogPostForm()})

def create_blogpost(request):
	if request.method == 'POST':
		form = BlogPostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.timestamp=datetime.now()
			post.save() #返回Blog模型实例s
	return HttpResponseRedirect('/blog/')

class BlogPostForm(forms.Form):
	title = forms.CharField(max_length=150)
	body = forms.CharField(widget=forms.Textarea(attrs={'row':3,'cols':60}))
	timestamp = forms.DateTimeField()