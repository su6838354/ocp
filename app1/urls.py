#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: urls.py
@time: 2017/2/11 0011 下午 1:23
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_admin$', views.add_admin, name='add_admin'),
    url(r'^get_admins$', views.get_admins, name='get_admins'),

    url(r'^add_user', views.add_user, name='add_user'),

    url(r'^add__user', views.add__user, name='add__user'),

    url(r'^add_activity', views.add_activity, name='add_activity'),

    url(r'^add_act_join_log', views.add_act_join_log, name='add_act_join_log'),

    url(r'^add_act_registration', views.add_act_registration, name='add_act_registration'),

]
