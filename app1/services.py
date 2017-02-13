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
        if admin_id and admin_id[0] != '':
            admin = models.Admins.objects.get(pid=admin_id[0])
            act_join_log['admin'] = admin

        userLocationArr_id = act_join_log.get('userLocationArr')
        if userLocationArr_id:
            userLocationArr = models.Admins.objects.get(pid=userLocationArr_id)
            act_join_log['userLocationArr'] = userLocationArr

        activity_id = act_join_log.get('activity')
        if activity_id:
            activity = models.Activities.objects.get(objectId=activity_id)
            act_join_log['activity'] = activity

        userGroupArr_id = act_join_log.get('userGroupArr')
        if userGroupArr_id:
            userGroupArr = models.Admins.objects.get(pid=userLocationArr_id)
            act_join_log['userGroupArr'] = userGroupArr

        user_id = act_join_log.get('user')
        if user_id:
            user = models.Users.objects.get(pid=user_id)
            act_join_log['user'] = user

        act_join_log = models.ActJoinLog.build(act_join_log)
        act_join_log.save()
        return {'code': 0}

    """---------------------------------------------------"""
    def add_act_registration(self, act_registration):
        admin_id = act_registration.get('admin')
        if admin_id:
            admin = models.Admins.objects.get(pid=admin_id)
            act_registration['admin'] = admin

        userLocationArr_id = act_registration.get('userLocationArr')
        if userLocationArr_id:
            userLocationArr = models.Admins.objects.get(pid=userLocationArr_id)
            act_registration['userLocationArr'] = userLocationArr

        activity_id = act_registration.get('activity')
        if activity_id:
            activity = models.Activities.objects.get(objectId=activity_id)
            act_registration['activity'] = activity

        userGroupArr_id = act_registration.get('userGroupArr')
        if userGroupArr_id:
            userGroupArr = models.Admins.objects.get(pid=userGroupArr_id)
            act_registration['userGroupArr'] = userGroupArr

        user_id = act_registration.get('user')
        if user_id:
            user = models.Users.objects.get(pid=user_id)
            act_registration['user'] = user

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


