from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def mul(x, y):
    print("%d * %d = %d" % (x, y, x * y))
    return x * y


@shared_task
def sub(x, y):
    time.sleep(10)
    print("%d - %d = %d" % (x, y, x - y))
    return x - y
