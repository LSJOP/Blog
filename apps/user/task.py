from celery import task
from django.conf import settings
from django.core.mail import send_mail  # 导入发送邮件函数


def send_register_success_mail(username, password, email):
    """发送注册成功邮件"""
    message = '<h1>欢迎您成为天天生鲜注册会员</h1>请记好您的注册信息:<br/>用户名:' + username + '<br/>密码:' + password
    send_mail('Hello,Python', '', settings.EMAIL_FROM, [email], html_message=message)
