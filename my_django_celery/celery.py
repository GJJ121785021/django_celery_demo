# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_celery.settings')  # 设置django环境

app = Celery('my_django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY') #  使用CELERY_ 作为前缀，在settings中写配置
# app.config_from_object('django.conf:settings')

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # 发现任务文件每个app下的task.py
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # dumps its own request information
