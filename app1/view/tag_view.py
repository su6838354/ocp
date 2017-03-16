#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: tag_view.py
@time: 2017/3/13 0013 下午 10:46
"""

import json
from app1.service.tag_service import TagService
import traceback

service = TagService()


def add_update_tag(request):
    params = json.loads(request.body)
    res = service.add_update_tag(params)
    return res


def add_update_activity2tag(request):
    params = json.loads(request.body)
    res = service.add_update_activity2tag(params)
    return res


def delete_activity2tag(request):
    params = json.loads(request.body)
    res = service.delete_activity2tag(params)
    return res


def get_tags(request):
    params = json.loads(request.body)
    res = service.get_tags(params)
    return res


def delete_tags(request):
    params = json.loads(request.body)
    res = service.delete_tags(params)
    return res
