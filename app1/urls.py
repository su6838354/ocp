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
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^add__user$', views.add__user, name='add__user'),
    url(r'^add_activity$', views.add_activity, name='add_activity'),
    url(r'^add_act_join_log$', views.add_act_join_log, name='add_act_join_log'),
    url(r'^add_act_registration$', views.add_act_registration, name='add_act_registration'),

    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^get_user$', views.get_user, name='get_user'),
    url(r'^update_user$', views.update_user, name='update_user'),
    url(r'^update_user_checkin$', views.update_user_checkin, name='update_user_checkin'),
    url(r'^create_user_admin$', views.create_user_admin, name='create_user_admin'),

    url(r'^get_admins$', views.get_admins, name='get_admins'),
    url(r'^get_admin$', views.get_admin, name='get_admin'),
    url(r'^update_admin$', views.update_admin, name='update_admin'),

    url(r'^get_activity$', views.get_activity, name='get_activity'),
    url(r'^get_activities$', views.get_activities, name='get_activities'),
    url(r'^get_activities_by_join$', views.get_activities_by_join, name='get_activities_by_join'),
    url(r'^update_activity$', views.update_activity, name='update_activity'),
    url(r'^create_activity$', views.create_activity, name='create_activity'),

    url(r'^get_act_registration_count$', views.get_act_registration_count, name='get_act_registration_count'),
    url(r'^get_act_registration$', views.get_act_registration, name='get_act_registration'),
    url(r'^create_act_registration$', views.create_act_registration, name='create_act_registration'),

    url(r'^get_act_join_log$', views.get_act_join_log, name='get_act_join_log'),
    url(r'^create_act_join_log$', views.create_act_join_log, name='create_act_join_log'),
    url(r'^update_act_join_log_extra$', views.update_act_join_log_extra, name='update_act_join_log_extra'),
    url(r'^update_activity_status', views.update_activity_status, name='update_activity_status'),

    #-------------------------------------------------------------------------------
    url(r'^get_user_checkin$', views.get_user_checkin, name='get_user_checkin'),
    url(r'^get_users$', views.get_users, name='get_users'),

    url(r'^add_update_tag$', views.add_update_tag, name='add_update_tag'),
    url(r'^add_update_activity2tag$', views.add_update_activity2tag, name='add_update_activity2tag'),
    url(r'^delete_activity2tag$', views.delete_activity2tag, name='delete_activity2tag'),
    url(r'^get_tags$', views.get_tags, name='get_tags'),
    url(r'^delete_tags$', views.delete_tags, name='delete_tags'),
    url(r'^delete_admin$', views.delete_admin, name='delete_admin'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
]
