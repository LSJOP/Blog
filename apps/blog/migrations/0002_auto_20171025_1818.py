# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contatc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('subject', models.CharField(max_length=60, verbose_name='主题')),
                ('email', models.EmailField(max_length=20, verbose_name='邮箱')),
                ('message', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '联系',
                'verbose_name_plural': '联系',
                'db_table': 'blog_Contatc',
            },
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
            ],
        ),
    ]