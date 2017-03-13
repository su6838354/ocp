# encoding: utf-8
from django.shortcuts import render

# Create your views here.

from app1.view._user_view import *
from app1.view.user_view import *
from app1.view.admin_view import *
from app1.view.activity_view import *
from app1.view.tag_view import *



# def get_admin(request):
#     pid = json.loads(request.body).get('pid')
#     res = service.get_admin(pid)
#     return JsonResponse(res)












