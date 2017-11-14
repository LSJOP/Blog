#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blog.settings")

    from django.core.management import execute_from_command_line

    # 解决root用户不能启动celery问题
    os.environ.setdefault('C_FORCE_ROOT', 'true')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{PATH TO SETTINGS FILE}')

    execute_from_command_line(sys.argv)
