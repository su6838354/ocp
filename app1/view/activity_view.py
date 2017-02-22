#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: activity_view.py
@time: 2017/2/21 0021 上午 12:06
"""
import json
from app1.services import Services

service = Services()

def add_activity(request):
    body_json = json.loads(request.body)
    res = service.add_activity(body_json)
    return res

def add_act_join_log(request):
    body_json = json.loads(request.body)
    res = service.add_act_join_log(body_json)
    return res

def add_act_registration(request):
    body_json = json.loads(request.body)
    res = service.add_act_registration(body_json)
    return res

def get_activity(request):
    body_json = json.loads(request.body)
    objectId = body_json.get('objectId')
    res = service.get_activity(objectId)
    return res

def get_activities(request):
    params = json.loads(request.body)
    res = service.get_activities(params)
    return res

def create_activity(request):
    params = json.loads(request.body)
    res = service.create_activity(params)
    return res


def get_act_registration(request):
    params = json.loads(request.body)
    res = service.get_act_registration(params)
    return res

def create_act_registration(request):
    params = json.loads(request.body)
    res = service.create_act_registration(params)
    return res

def get_act_join_log(request):
    params = json.loads(request.body)
    res = service.get_act_join_log(params)
    return res

def create_act_join_log(request):
    params = json.loads(request.body)
    res = service.create_act_join_log(params)
    return res