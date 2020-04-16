from __future__ import absolute_import

import time

from celery import task

from celery import shared_task


# from celery.task import tasks
# from celery.task import Task
# class AddClass(Task):
#    def run(x,y):
#        print "%d + %d = %d"%(x,y,x+y)
#        return x+y
# tasks.register(AddClass)


@shared_task
def mul(x, y):
    print("%d * %d = %d" % (x, y, x * y))
    return x * y


@shared_task
def sub(x, y):
    time.sleep(10)
    print("%d - %d = %d" % (x, y, x - y))
    return x - y
