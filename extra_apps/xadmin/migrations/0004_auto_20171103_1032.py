# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0003_auto_20160715_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='content_type',
            field=models.ForeignKey(verbose_name='content type', blank=True, to_field=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', to_field=django.db.models.deletion.CASCADE),
        ),
    ]
