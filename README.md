# django_celery_demo


#使用django-celery-beat 定时调度任务

- 在<a href="https://github.com/GJJ121785021/django_celery_demo/tree/master">配置好celery并能正常使用后</a>

1.安装： pip install django-celery-beat

2.将django_celery_beat模块添加到INSTALLED_APPS   Django项目中settings.py：

INSTALLED_APPS = (\
    'django_celery_beat',\
)

3.应用Django数据库迁移，以便创建必要的表： python manage.py migrate


4.另外需要使用调度程序启动celery worker服务
celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

为了方便直接在设置中添加：
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'



## 注意
1.在admin中添加任务时，可在任务中添加函数所需的参数

2.在启动任务进入admin中后会报错

t = DEBUG_ENGINE.from_string(fh.read())　　\
　　UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: illegal multibyte sequence
  
直接修改源码：
打开django/views下的debug.py文件，转到line331行：
with Path(CURRENT_DIR, 'templates', 'technical_500.html').open() as fh

将其改成：
    with Path(CURRENT_DIR, 'templates', 'technical_500.html').open(encoding="utf-8") as fh
