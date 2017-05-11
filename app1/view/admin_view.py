#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: admin_view.py
@time: 2017/2/21 0021 上午 12:05
"""
import json
from app1.services import Services
from app1.service.admin_service import AdminService

service = AdminService()
from app1.util import log

def add_admin(request):
    body_json = json.loads(request.body)
    res = service.add_admin(body_json)
    return res


def get_admins(request):
    params = json.loads(request.body)
    res = service.get_admins(params)
    log.info("======3")
    return res


def get_admin(request):
    params = json.loads(request.body)
    res = service.get_admin(params)
    return res


def update_admin(request):
    params = json.loads(request.body)
    res = service.update_admin(params)
    return res

def delete_admin(request):
    params = json.loads(request.body)
    res = service.delete_admin(params)
    return res
