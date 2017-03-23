#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: user_view.py
@time: 2017/2/21 0021 上午 12:05
"""

import json
from app1.service.user_service import UserService
import traceback

service = UserService()


def add_user(request):
    body_json = json.loads(request.body)
    res = service.add_user(body_json)
    return res

def create_user_admin(request):
    params = json.loads(request.body)
    try:
        res = service.create_user_admin(params)
    except Exception, e:
        traceback.print_exc()
        res = {'code': 110, 'msg': e.message}
    return res


def get_user(request):
    body_json = json.loads(request.body)
    pid = body_json.get('pid')
    res = service.get_user(pid)
    return res

def update_user(request):
    params = json.loads(request.body)
    res = service.update_user(params)
    return res

def update_user_checkin(request):
    params = json.loads(request.body)
    res = service.update_user_checkin(params)
    return res

def get_user_checkin(request):
    params = json.loads(request.body)
    res = service.get_user_checkin(params)
    return res



def get_users(request):
    params = json.loads(request.body)
    res = service.get_users(params)
    return res

def delete_user(request):
    params = json.loads(request.body)
    res = service.delete_user(params)
    return res