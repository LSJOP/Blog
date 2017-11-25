import logging
import time

from django.conf import settings

from django.core.mail import send_mail  # 导入发送邮件函数

from Celery_Task.celery import app


@app.task
def send_register_success_mail(username, email, type ='register'):
    if type == 'register':
        """发送注册成功邮件"""
        message = '<h1>欢迎您成为起風了注册会员</h1>请记好您的注册信息:<br/>用户名:' + username + '<br/><a href="http://linsijian.cn/">起風了</a>'
        send_mail(username, ' ', settings.EMAIL_FROM, [email], html_message=message)
