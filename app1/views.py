# encoding: utf-8
from django.shortcuts import render

# Create your views here.

from django import http
from services import Services
import json

def JsonResponse(res):
    response = http.JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

service = Services()

"""------------------------------"""
def add_admin(request):
    body_json = json.loads(request.body)
    res = service.add_admin(body_json)
    return JsonResponse(res)

"""------------------------------"""
def add_user(request):
    body_json = json.loads(request.body)
    res = service.add_user(body_json)
    return JsonResponse(res)

"""------------------------------"""
def add__user(request):
    body_json = json.loads(request.body)
    res = service.add__user(body_json)
    response = JsonResponse(res)
    return response
"""------------------------------"""
def add_activity(request):
    body_json = json.loads(request.body)
    res = service.add_activity(body_json)
    return JsonResponse(res)
"""------------------------------"""
def add_act_join_log(request):
    body_json = json.loads(request.body)
    res = service.add_act_join_log(body_json)
    return JsonResponse(res)

"""------------------------------"""
def add_act_registration(request):
    body_json = json.loads(request.body)
    res = service.add_act_registration(body_json)
    return JsonResponse(res)


"-------------#################################-------------"
def get_user(request):
    body_json = json.loads(request.body)
    pid = body_json.get('pid')
    res = service.get_user(pid)
    return JsonResponse(res)

def get_activity(request):
    body_json = json.loads(request.body)
    objectId = body_json.get('objectId')
    res = service.get_activity(objectId)
    return JsonResponse(res)

def get_admins(request):
    res = service.get_admins()
    return JsonResponse(res)

def get_admin(request):
    pid = json.loads(request.body).get('pid')
    res = service.get_admin(pid)
    return JsonResponse(res)

def get_activities(request):
    params = json.loads(request.body)
    res = service.get_activities(params)
    return JsonResponse(res)

def get_act_registration(request):
    params = json.loads(request.body)
    res = service.get_act_registration(params)
    return JsonResponse(res)

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

