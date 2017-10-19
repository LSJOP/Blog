# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 11:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('body', models.TextField(verbose_name='文章')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'db_table': 'blog_classfiy',
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Classfiy', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, db_table='Article_to_Tag', to='blog.Tag', verbose_name='标签'),
        ),
    ]
