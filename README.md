# django_celery_demo

使用python == 3.5 或 3.6  (3.7以上会因为celery内有async关键字而报错（可以改但有点麻烦）)

pip install celery
pip install eventlet  （Windows需安装这个，并且在启动命令后加-P eventlet）


启动celery任务
celery -A <project-name> worker -l info -P eventlet

启动web 服务
python manage.py runserver



## 有几点需要注意
1.不要安装django-celery ，安装后似乎会对celery有影响，之前的配置需要修改成代码中被注释的部分（注释的也不完善）\
2.配置中有两个redis url， 如果写错了这个配置  'redis://:123456@127.0.0.1:6379/0'\
        并且库不一样的，会报错（迭代深度的error）\
3.如果在配置都正确的情况下，先启动web服务并且调度任务（进入会调度异步任务的url），任务会被添加到redis队列中，在稍后运行worker，（启动Celery Worker服务，来开始监听并执行任务后，）任务会自动被执行
