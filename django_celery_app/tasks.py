from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task


@shared_task
def mul(x, y):
    print("%d * %d = %d" % (x, y, x * y))
    return x * y


@shared_task
def sub(x, y):
    time.sleep(10)
    print("%d - %d = %d" % (x, y, x - y))
    return x - y


# @periodic_task(run_every=crontab(minute='*', hour='9-12'))
@periodic_task(run_every=10)
def beat_test():
    return 'iss  ra  beara!!'
