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

def get_admins(request):
    res = service.get_admins()
    return JsonResponse(res)

def get_admin(request):
    pid = json.loads(request.body).get('pid')
    res = service.get_admin(pid)
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