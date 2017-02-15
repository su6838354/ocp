#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: services.py
@time: 2017/2/11 0011 下午 1:23
"""

import models
from django.forms.models import model_to_dict
from django.core import serializers
import json
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

class Services(object):
    def __index__(self):
        pass

    def __check_id_tuple(self, pid_tuple):
        if pid_tuple and len(pid_tuple[0]) == 24:
            return True
        else:
            return False


    """---------------------------------------------------"""
    def add_admin(self, admin):
        admin = models.Admins.build(admins=admin)
        admin.save()
        return {'code': 0}

    def get_admins(self):
        admins = models.Admins.objects.values()
        # admins_json = serializers.serialize('json', admins)
        admins_list = list(admins)
        return {'code': 0, 'data': admins_list}

    def get_admin(self, pid):
        admin = models.Admins.objects.get(pid=pid)
        admin_dict = model_to_dict(admin)
        return {'code': 0, 'data': admin_dict}

    """---------------------------------------------------"""
    def add_user(self, user):
        group_id = user.get('group')
        if self.__check_id_tuple(group_id):
            group = models.Admins.objects.get(pid=group_id[0])
            user['group'] = group
        else:
            user['group'] = None

        location_id = user.get('location')
        if self.__check_id_tuple(location_id):
            location = models.Admins.objects.get(pid=location_id[0])
            user['location'] = location
        else:
            user['location'] = None

        checkin = user.get('checkin')
        if checkin:
            checkin = json.dumps(checkin)
            user['checkin'] = checkin
        else:
            user['checkin'] = None

        birth = user.get('birth')
        if birth:
            birth = birth['iso']
            user['birth'] = birth
        else:
            user['birth'] = None

        user = models.Users.build(user)
        user.save()
        return {'code': 0}

    """---------------------------------------------------"""
    def add__user(self, _user):
        _user = models._User.build(_user)
        _user.save()
        return {'code': 0}

    """---------------------------------------------------"""
    def add_activity(self, activity):
        admin_id = activity.get('admin')
        if self.__check_id_tuple(admin_id):
            admin = models.Admins.objects.get(pid=admin_id[0])
            activity['admin'] = admin
        else:
            activity['admin'] = None

        activity = models.Activities.build(activity)
        activity.save()
        return {'code': 0}

    """---------------------------------------------------"""
    def add_act_join_log(self, act_join_log):
        admin_id = act_join_log.get('admin')
        if self.__check_id_tuple(admin_id):
            admin = models.Admins.objects.get(pid=admin_id[0])
            act_join_log['admin'] = admin
        else:
            act_join_log['admin'] = None

        userLocationArr_id = act_join_log.get('userLocationArr')
        if self.__check_id_tuple(userLocationArr_id):
            userLocationArr = models.Admins.objects.get(pid=userLocationArr_id[0])
            act_join_log['userLocationArr'] = userLocationArr
        else:
            act_join_log['userLocationArr'] = None

        activity_id = act_join_log.get('activity')
        if self.__check_id_tuple(activity_id):
            activity = models.Activities.objects.get(objectId=activity_id[0])
            act_join_log['activity'] = activity
        else:
            act_join_log['activity'] = None

        userGroupArr_id = act_join_log.get('userGroupArr')
        if self.__check_id_tuple(userGroupArr_id):
            userGroupArr = models.Admins.objects.get(pid=userGroupArr_id[0])
            act_join_log['userGroupArr'] = userGroupArr
        else:
            act_join_log['userGroupArr'] = None

        user_id = act_join_log.get('user')
        if self.__check_id_tuple(user_id):
            user = models.Users.objects.get(pid=user_id[0])
            act_join_log['user'] = user
        else:
            act_join_log['user'] = None

        act_join_log = models.ActJoinLog.build(act_join_log)
        act_join_log.save()
        return {'code': 0}

    """---------------------------------------------------"""
    def add_act_registration(self, act_registration):
        admin_id = act_registration.get('admin')
        if self.__check_id_tuple(admin_id):
            admin = models.Admins.objects.get(pid=admin_id[0])
            act_registration['admin'] = admin
        else:
            act_registration['admin'] = None

        userLocationArr_id = act_registration.get('userLocationArr')
        if self.__check_id_tuple(userLocationArr_id):
            userLocationArr = models.Admins.objects.get(pid=userLocationArr_id[0])
            act_registration['userLocationArr'] = userLocationArr
        else:
            act_registration['userLocationArr'] = None

        activity_id = act_registration.get('activity')
        if self.__check_id_tuple(activity_id):
            activity = models.Activities.objects.get(objectId=activity_id[0])
            act_registration['activity'] = activity
        else:
            act_registration['activity'] = None

        userGroupArr_id = act_registration.get('userGroupArr')
        if self.__check_id_tuple(userGroupArr_id):
            userGroupArr = models.Admins.objects.get(pid=userGroupArr_id[0])
            act_registration['userGroupArr'] = userGroupArr
        else:
            act_registration['userGroupArr'] = None

        user_id = act_registration.get('user')
        if self.__check_id_tuple(user_id):
            user = models.Users.objects.get(pid=user_id[0])
            act_registration['user'] = user
        else:
            act_registration['user'] = None

        act_registration = models.ActRegistration.build(act_registration)
        act_registration.save()
        return {'code': 0}

    def get_user(self, pid):
        if pid:
            user = models.Users.objects.get(pid=pid)
            user.checkin = json.loads(user.checkin)
            user_dict = model_to_dict(user)
            user_dict['group'] = model_to_dict(user.group)
            user_dict['location'] = model_to_dict(user.location)
            return {'code': 0, 'data': user_dict}
        else:
            return {'code': 100, 'data': {}}

    def get_activity(self, objectId):
        if objectId:
            activity = models.Activities.objects.get(objectId=objectId)
            activity_dict = model_to_dict(activity)
            activity_dict['admin'] = model_to_dict(activity.admin)
            return {'code': 0, 'data': activity_dict}
        else:
            return {'code': 100, 'data': {}}

    def get_activities(self, params):
        isDelete = params.get('isDelete')
        isShow = params.get('isShow')
        limit = params.get('limit')
        skip = params.get('skip')
        activities = models.Activities.objects.filter(
            ~Q(isDelete=isDelete), ~Q(isShow=isShow)
        ).order_by('-createdAt')[skip: skip+limit]
        owner_fields = [f.name for f in models.Activities._meta.get_fields()]
        fields = owner_fields + ['admin__type', 'admin__objectId', 'admin__name', 'admin__username']
        activities_list = list(activities.values(*fields))
        return {'code': 0, 'data': list(activities_list)}