#！/bin/bash
source /data/suyuan/ocp_env/bin/activate
nohup gunicorn ocp.wsgi:application -k gevent -b 0.0.0.0:3391 --reload &
