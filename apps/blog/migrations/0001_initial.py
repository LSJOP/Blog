# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('body', models.TextField(verbose_name='文章')),
                ('excerpt', models.CharField(max_length=200, verbose_name='摘要', blank=True)),
                ('read_num', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'db_table': 'blog_article',
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Classfiy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('name', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'db_table': 'blog_classfiy',
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('comment', models.CharField(max_length=1024, verbose_name='评论')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
                ('email', models.EmailField(max_length=20, verbose_name='邮箱')),
                ('addr', models.CharField(max_length=40, verbose_name='用户发表评论时的地址')),
                ('article', models.ForeignKey(to='blog.Article', verbose_name='所属文章')),
            ],
            options={
                'db_table': 'blog_comment',
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Contatc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('subject', models.CharField(max_length=60, verbose_name='主题')),
                ('email', models.EmailField(max_length=20, verbose_name='邮箱')),
                ('message', models.TextField(verbose_name='内容')),
            ],
            options={
                'db_table': 'blog_Contatc',
                'verbose_name': '联系',
                'verbose_name_plural': '联系',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('name', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'db_table': 'blog_tag',
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='classfiy',
            field=models.ForeignKey(to='blog.Classfiy', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签', blank=True),
        ),
    ]
