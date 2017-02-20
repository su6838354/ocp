#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: _user_view.py
@time: 2017/2/21 0021 上午 12:09
"""

import json
from app1.services import Services
from django.http import JsonResponse

service = Services()


def add__user(request):
    body_json = json.loads(request.body)
    res = service.add__user(body_json)
    return res

def login(request):
    params = json.loads(request.body)
    user_role = params.get('userRole')
    user_name = params.get('userName')
    user_pwd = params.get('userPwd')
    res = service.login(user_role, user_name, user_pwd)
    response = JsonResponse(res)
    if res['code'] == 0:
        response.set_cookie('user_name', user_name, 60*60*24) # 24h
        response.set_cookie('user_role', user_role, 60 * 60 * 24)  # 24h
        response.set_cookie('user_pid', res.get('data').get('pid'))
    return response


def logout(request):
    response = JsonResponse({'code': 0, 'data': None})
    response.delete_cookie('user_name')
    request.delete_cookie('user_role')
    request.delete_cookie('user_pid')
    return response