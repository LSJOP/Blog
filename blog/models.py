#-*-coding:utf-8-*-
from django.db import models
from django import forms

# Create your models here.

class Meta:
	#-timestamp按时间逆序排列
	ordering = ('-timestamp',)

class BlogPost(models.Model):
	title =models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		exclude = ('timestamp',)
