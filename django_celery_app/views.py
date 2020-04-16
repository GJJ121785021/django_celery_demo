from django.http import HttpResponse
from django.shortcuts import render

from django_celery_app.tasks import mul, sub


def mul_view(request):
    mul(2,4)
    return HttpResponse('mul')


def sub_view(request):
    sub.delay(2,5)
    return HttpResponse('sub')