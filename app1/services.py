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
import util
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

    def get_admins(self, params):
        isShow = params.get('isShow')
        limit = params.get('limit')
        skip = params.get('skip')
        admins = models.Admins.objects.filter(Q(isShow=isShow)).values()[skip: skip+limit]
        # admins_json = serializers.serialize('json', admins)
        admins_list = list(admins)
        return {'code': 0, 'data': admins_list}

    def get_admin(self, params):
        pid = params.get('pid')
        admin = models.Admins.objects.get(pid=pid)
        admin_dict = model_to_dict(admin)
        return {'code': 0, 'data': admin_dict}

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
            if user.group != None:
                user_dict['group'] = model_to_dict(user.group)
            if user.location != None:
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
        admin_pid = params.get('admin', '')
        activities = models.Activities.objects.filter(
            ~Q(isDelete=isDelete), ~Q(isShow=isShow), Q(admin__pid__contains=admin_pid)
        ).order_by('-createdAt')[skip: skip+limit]
        owner_fields = [f.name for f in models.Activities._meta.get_fields()]
        fields = owner_fields + ['admin__type', 'admin__objectId', 'admin__name', 'admin__username']
        activities_list = list(activities.values(*fields))
        return {'code': 0, 'data': list(activities_list)}

    def create_activity(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        admin_id = params.get('admin')
        if admin_id is not None and admin_id != '':
            admin = models.Admins.objects.get(pid=admin_id)
            params['admin'] = admin
        else:
            params['admin'] = None

        activity = models.Activities.build(params)
        activity.save()
        return {'code': 0, 'data': {'objectId': activity.objectId}, 'msg': '保存成功'}

    def get_act_registration(self, params):
        activity_objectId = params.get('activity', '')
        user_pid = params.get('user', '')
        act_registration_count = models.ActRegistration.objects.filter(
            Q(activity=activity_objectId), Q(user__pid__contains=user_pid)
        ).count()
        return {'code': 0, 'data': {'count': act_registration_count}}

    def login(self, user_role, user_name, user_pwd):
        if user_role == "Admins":
            admins = models.Admins.objects.filter(Q(username=user_name), Q(pwd=user_pwd)).values()
            if len(list(admins)) == 1:
                admin = admins[0]
                return {'code': 0, 'data': admin}
            return {'code': 111, 'data': None, 'msg': '不存在管理员'}
        elif user_role == "Users":
            if user_pwd == '123456':
                users = models.Users.objects.filter(Q(username=user_name)).values()
                if len(list(users)) == 1:
                    user = users.first()
                    user_dict = user
                    if user.get('group_id') is not None:
                        user_dict['group'] = model_to_dict(models.Admins.objects.get(pid=user_dict['group_id']))
                    if user.get('location_id') is not None:
                        user_dict['location'] = model_to_dict(models.Admins.objects.get(pid=user_dict['location_id']))
                    user_dict['checkin'] = json.loads(user_dict.get('checkin', {}))
                    return {'code': 0, 'data': user_dict}
            return {'code': 111, 'data': None, 'msg': '不存在用户'}
        else:
            return {'code': 110, 'data': None, 'msg': 'userRole error'}

    def create_act_registration(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        params['admin'] = models.Admins.objects.get(pid=params.get('admin'))
        params['userLocationArr'] = models.Admins.objects.get(pid=params.get('userLocationArr'))
        params['activity'] = models.Activities.objects.get(objectId=params.get('activity'))
        params['userGroupArr'] = models.Admins.objects.get(pid=params.get('userGroupArr'))
        params['user'] = models.Users.objects.get(pid=params.get('user'))
        if params.get('isInner') is None:
            params['isInner'] = False
        act_registeration = models.ActRegistration.build(params)
        act_registeration.save()
        return {'code': 0, 'data': {'objectId': act_registeration.objectId}, 'msg': 'save success'}

    def get_act_join_log(self, params):
        user_id = params.get('user')
        admin_id = params.get('admin', '')
        act_join_logs = models.ActJoinLog.objects.filter(
            Q(user=user_id),
            Q(admin__pid__contains=admin_id)
        ).values()
        act_join_logs_list = list(act_join_logs)
        return {'code': 0, 'data': act_join_logs_list}

    def create_act_join_log(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        if params['admin'] is not None and  params['admin'] != '':
            params['admin'] = models.Admins.objects.get(pid=params.get('admin'))
        else:
            params['admin'] = None

        if params['userLocationArr'] is not None and params['userLocationArr'] != '':
            params['userLocationArr'] = models.Admins.objects.get(pid=params.get('userLocationArr'))
        else:
            params['userLocationArr'] = None

        if params['activity'] is not None and params['activity'] != '':
            params['activity'] = models.Activities.objects.get(objectId=params.get('activity'))
        else:
            params['activity'] = None

        if params['userGroupArr'] is not None and params['userGroupArr'] != '':
            params['userGroupArr'] = models.Admins.objects.get(pid=params.get('userGroupArr'))
        else:
            params['userGroupArr'] = None

        if params['user'] is not None and params['user'] != '':
            params['user'] = models.Users.objects.get(pid=params.get('user'))
        else:
            params['user'] = None

        if params.get('isInner') is None:
            params['isInner'] = False
        act_registeration = models.ActJoinLog.build(params)
        act_registeration.save()
        return {'code': 0, 'data': {'objectId': act_registeration.objectId}, 'msg': 'save success'}