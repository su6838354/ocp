#！/bin/bash
nohup /data/suyuan/bin/gunicorn ocp.wsgi:application -k gevent -b 0.0.0.0:3390 --reload &