#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: util.py
@time: 2017/2/19 0019 上午 11:12
"""
import uuid
import datetime
import math
import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='ocp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

log = logging

def get_uuid_24():
    tmp = uuid.uuid1()
    tmp = str(tmp).replace('-', '')
    return tmp[0:24]


def get_now_tuc():
    return str(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))


def make_pagination(count, page_index, limit):
    return {'pagination':
        {
            'count': count,
            'limit': limit,
            'page_count': int(math.ceil(float(count) / limit)),
            'page_index': page_index
        }
    }
