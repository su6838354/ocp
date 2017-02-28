#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: allow_csrf.py
@time: 2017/2/20 0020 下午 11:55
"""

from django import http
from django.utils.deprecation import MiddlewareMixin


class AllowCsrf(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        if type(response) == dict:
            response = http.JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
