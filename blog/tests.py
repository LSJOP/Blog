"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
#-*-coding:utf-8-*-
from django.test import TestCase
from datetime import datetime
from django.test.client import Client
from blog.models import BlogPost

class BlogPostTest(TestCase):
	def test_obj_create(self):
		BlogPost.objects.create(title='raw title',body='raw body',timestamp=datetime.now())
		self.assertEqual(1,BlogPost.objects.count())
		self.assertEqual('raw title',BlogPost.objects.get(id=1).title)

	def test_home(self):
		response = self.client.get('/blog/')
		self.failUnlessEqual(response.status_code,200)

	def test_slash(self):
		response = self.client.get('/')
		self.assertIn(response.status_code,(301,302))

	def test_empty_create(self):
		response = self.Client.get('/blog/create/')
		self.assertIn(response.status_code,(301,302))

	def test_post_create(self):
		response = self.client.post('/blog/create',{'title':'post title','body':'post body',})
		self.assertIn(response.status_code,(301,302))
		self.assertEqual(1,BlogPost.objects.count())
		self.assertEqual('post title',BlogPost.objects.get(id=1).title)