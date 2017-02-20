#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: app1_check_login.py
@time: 2017/2/19 0019 上午 11:00
"""

from django.utils.deprecation import MiddlewareMixin
from django import http
from ocp.settings import NO_LOGIN

def JsonResponse(res):
    response = http.JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

class CheckLogin(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        return None
        if request.path not in NO_LOGIN:
            user_name = request.COOKIES.get('user_name')
            if user_name == None:
                return JsonResponse({'code': 111, 'data': None, 'msg': 'need login'})