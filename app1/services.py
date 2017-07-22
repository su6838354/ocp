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
from django.db.models import F
from django.core import serializers
import json
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
import traceback
from util import log


class Services(object):
    def __index__(self):
        pass

    def _get_q_show(self, isShow):
        if isShow == '-1':
            q_show = ~Q(isShow='-1')
        else:
            q_show = Q(isShow=isShow)
        return q_show

    def __check_id_tuple(self, pid_tuple):
        if pid_tuple and len(pid_tuple[0]) == 24:
            return True
        else:
            return False

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

    def create__user(self, password, username, userRole):
        objectId = util.get_uuid_24()
        _user = {
            "objectId": objectId,
            "password": password,
            "username": username,
            "emailVerified": False,
            "userRole": userRole,
            "mobilePhoneVerified": False,
            "createdAt": util.get_now_tuc(),
            "updatedAt": util.get_now_tuc()
        }
        _user = models._User.build(_user)
        _user.save()
        return _user.objectId

    def create_user_admin(self, params):
        # 创建_user
        userRole = params.get('userRole', 'Users')
        username = params.get('username', '123456')
        password = params.get('password', '123456')
        _user_objectId = self.create__user(password, username, userRole)
        objectId = util.get_uuid_24()
        isShow = params.get('isShow', '1')
        mobile = params.get('mobile')
        if userRole == "Admins":
            has_admin = models.Admins.objects.filter(
                username=username, isDelete=0
            )
            if len(list(has_admin)) > 0:
                return {'code': 113, 'msg': '相同的用户名存在'}
            admins_params = {
                'pid': _user_objectId,
                'objectId': objectId,
                'isShow': isShow,
                'pwd': password,
                'username': username,
                'name': params.get('name'),
                'type': params.get('type'),
                'person': params.get('person'),
                'address': params.get('address'),
                'mobile': mobile,
                'tel': params.get('tel'),
                'createdAt': util.get_now_tuc(),
                'updatedAt': util.get_now_tuc(),
                'flagNumber': params.get('flagNumber', ''),
                'group_type': params.get('group_type', 0),
                'parentId': params.get('parentId', ''),
            }
            admins = models.Admins.build(admins_params)
            admins.save()
            return {'code': 0, 'msg': '社区组织创建成功', 'data': {'pid': admins.pid}}
        else:
            has_user = models.Users.objects.filter(
                username=username
            )
            if len(list(has_user)) > 0:
                return {'code': 113, 'msg': '相同的用户名存在'}
            user_params = {
                'pid': _user_objectId,
                'objectId': objectId,
                'isShow': isShow,
                'username': username,
                'realname': params.get('realname', '123456'),
                'sex': params.get('sex', '男'),
                'idcard': params.get('idcard', ''),
                'mobile': mobile,
                'birth': params.get('birth'),
                'flagNumber': params.get('flagNumber'),
                'political': params.get('political'),
                # 'group_type': params.get('group_type'),
                # 'parentId': params.get('parentId', ''),
                'createdAt': util.get_now_tuc(),
                'updatedAt': util.get_now_tuc()
            }
            user = models.Users.build(user_params)

            group_id = params.get('group')
            if group_id is not None and group_id != '':
                group = models.Admins.objects.filter(pid=group_id, isDelete=0)
                if len(group) > 0:
                    user.group = group[0]

            location_id = params.get('location')
            if location_id is not None and location_id != '':
                location = models.Admins.objects.filter(pid=location_id, isDelete=0)
                if len(location) > 0:
                    user.location = location[0]

            user.save()
            return {'code': 0, 'msg': '普通用户创建成功', 'data': {'pid': user.pid}}

    def update_user_checkin(self, params):
        user = params.get('user', '')
        checkin = params.get('checkin')

        if checkin:
            checkin = json.dumps(checkin)
            checkin = checkin
        else:
            checkin = None

        models.Users.objects.filter(Q(pid=user)).update(
            checkin=checkin
        )
        return {'code': 0, 'msg': '更新成功'}

    def update_user(self, params):
        user = params
        group_id = user.get('group')
        try:
            group = models.Admins.objects.get(pid=group_id)
            user['group'] = group
        except:
            user['group'] = None

        location_id = user.get('location')
        try:
            location = models.Admins.objects.get(pid=location_id)
            user['location'] = location
        except:
            user['location'] = None

        checkin = user.get('checkin')
        if checkin:
            checkin = json.dumps(checkin)
            user['checkin'] = checkin
        else:
            user['checkin'] = None

        user['updatedAt'] = util.get_now_tuc()

        user = models.Users.build(user)
        user.save()
        return {'code': 0, 'msg': '更新成功', 'data': {'pid': user.pid}}

    """---------------------------------------------------"""

    def add__user(self, _user):
        _user = models._User.build(_user)
        _user.save()
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
            if user.checkin is not None:
                user.checkin = json.loads(user.checkin)
            user_dict = model_to_dict(user)
            if user.group != None:
                user_dict['group'] = model_to_dict(user.group)
            if user.location != None:
                user_dict['location'] = model_to_dict(user.location)
            return {'code': 0, 'data': user_dict}
        else:
            return {'code': 100, 'data': {}}

    def get_user_checkin(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        q_list = []
        checkin = params.get('checkin')
        if checkin is False:
            q_list.append(Q(checkin=None))
        else:
            q_list.append(~Q(checkin=None))

        group = params.get('group', '')
        if group != '':
            q_list.append(Q(group__pid__contains=group))

        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        q_list.append(q_show)

        q_list.append(Q(isDelete=0))
        users = models.Users.objects.filter(
            *q_list
            #    Q(checkin=None), Q(group__pid__contains=group), q_show
        )
        count = users.count()
        users_list = list(users[(page_index - 1) * limit: page_index * limit].values())
        res = {'code': 0, 'data': users_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def get_activities_by_join(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        join = params.get('join', False)
        admin = params.get('admin')
        user = params.get('user')
        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        isDelete = params.get('isDelete', '0')

        join_activities = models.ActJoinLog.objects.filter(
            Q(admin__pid=admin), Q(user__pid=user)
        ).values_list('activity__objectId', flat=True).distinct()
        if join is False:
            activities = models.Activities.objects. \
                filter(Q(admin__pid=admin), q_show, isDelete=isDelete).exclude(
                objectId__in=join_activities
            ).order_by('createdAt')
        else:
            activities = models.Activities.objects \
                .filter(Q(admin__pid=admin), q_show,
                        Q(objectId__in=join_activities), isDelete=isDelete).order_by('createdAt')
        count = activities.count()
        res = {'code': 0, 'data': list(activities.values())}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def get_act_registration(self, params):
        activity_objectId = params.get('activity', '')
        limit = params.get('limit', 10)
        page_index = params.get('page_index', 1)
        act_registration = models.ActRegistration.objects.filter(
            Q(activity=activity_objectId)
        ).order_by('-createdAt')
        count = act_registration.count()
        fileds = ['admin__pid', 'admin__type', 'admin__name', 'admin__username',
                  'userLocationArr__objectId', 'userLocationArr__type', 'userLocationArr__name',
                  'userLocationArr__username',
                  'activity__objectId', 'activity__title', 'activity__content',
                  'userGroupArr__objectId', 'userGroupArr__name', 'userGroupArr__username', 'userGroupArr__type',
                  'user__pid', 'user__realname', 'user__username', 'user__sex', 'user__group__name',
                  'user__mobile', 'user__political', 'user__job',
                  'objectId', 'createdAt'
                  ]
        act_registration_values = act_registration[(page_index - 1) * limit: page_index * limit].values(*fileds)
        res = {'code': 0, 'data': list(act_registration_values)}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def login(self, user_role, user_name, user_pwd):
        if user_role == "Admins":
            admins = models.Admins.objects.filter(Q(username=user_name), Q(pwd=user_pwd), Q(isDelete=0)).values()
            if len(list(admins)) == 1:
                admin = admins[0]
                return {'code': 0, 'data': admin}
            return {'code': 111, 'data': None, 'msg': '不存在管理员'}
        elif user_role == "Users":
            if user_pwd == '123456':
                users = models.Users.objects.filter(Q(username=user_name), Q(isDelete=0)).values()
                if len(list(users)) == 1:
                    user = users.first()
                    user_dict = user
                    if user.get('group_id') is not None:
                        user_dict['group'] = model_to_dict(models.Admins.objects.get(pid=user_dict['group_id']))
                    if user.get('location_id') is not None:
                        user_dict['location'] = model_to_dict(models.Admins.objects.get(pid=user_dict['location_id']))

                    checkin = user_dict.get('checkin')
                    if checkin is not None:
                        user_dict['checkin'] = json.loads(checkin)

                    checkin2016 = user_dict.get('checkin2016')
                    if checkin2016 is not None:
                        user_dict['checkin2016'] = json.loads(checkin2016)
                        print user_dict
                    return {'code': 0, 'data': user_dict}
            return {'code': 111, 'data': None, 'msg': '不存在用户'}
        elif user_role == "SuperAdmin":
            if user_name == "admin" and user_pwd == "admin":
                return {'code': 0, 'data': {'pid': '001'}, 'msg': 'admin login success'}
            return {'code': 110, 'data': {'pid': '001'}, 'msg': 'admin name or pwd error'}
        else:
            return {'code': 111, 'data': None, 'msg': 'role error'}

    def create_act_registration(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        try:
            params['admin'] = models.Admins.objects.get(pid=params.get('admin'))
        except:
            params['admin'] = None

        try:
            params['userLocationArr'] = models.Admins.objects.get(pid=params.get('userLocationArr'))
        except:
            params['userLocationArr'] = None

        params['activity'] = models.Activities.objects.get(objectId=params.get('activity'))
        try:
            params['userGroupArr'] = models.Admins.objects.get(pid=params.get('userGroupArr'))
        except:
            params['userGroupArr'] = None

        try:
            params['user'] = models.Users.objects.get(pid=params.get('user'))
        except:
            params['user'] = None
        if params.get('isInner') is None:
            params['isInner'] = False
        act_registeration = models.ActRegistration.build(params)
        act_registeration.save()
        return {'code': 0, 'data': {'objectId': act_registeration.objectId}, 'msg': 'save success'}

    def get_act_join_log(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        user_id = params.get('user', '')
        admin_id = params.get('admin', '')
        activity_id = params.get('activity', '')
        act_join_logs = models.ActJoinLog.objects.filter(
            Q(user__pid__contains=user_id),
            Q(admin__pid__contains=admin_id),
            Q(activity__objectId__contains=activity_id)
        ).order_by('-createdAt')
        count = act_join_logs.count()
        fileds = ['objectId', 'user__pid', 'user__realname', 'user__group__name',
                  'user__location__name', 'isInner', 'star', 'extra', 'activity__title', 'createdAt', 'mark']
        act_join_logs_values = act_join_logs[(page_index - 1) * limit: page_index * limit]. \
            values(*fileds)
        act_join_logs_list = list(act_join_logs_values)
        res = {'code': 0, 'data': act_join_logs_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def create_act_join_log(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        if params['admin'] is not None and params['admin'] != '':
            params['admin'] = models.Admins.objects.get(pid=params.get('admin'))
        else:
            params['admin'] = None

        if params['userLocationArr'] is not None and params['userLocationArr'] != '':
            params['userLocationArr'] = models.Admins.objects.get(pid=params.get('userLocationArr'))
        else:
            params['userLocationArr'] = None

        activity_id = params.get('activity')
        try:
            params['activity'] = models.Activities.objects.get(objectId=activity_id)
        except Exception, e:
            util.log.error(e.message)
            traceback.print_exc()
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

        models.Activities.objects.filter(objectId=activity_id).update(
            joinnum=F('joinnum') + 1
        )
        util.log.info('act_join_id:%s join activity_id:%s' % (act_registeration.objectId, activity_id))
        return {'code': 0, 'data': {'objectId': act_registeration.objectId}, 'msg': 'save success'}

    def update_act_join_log_extra(self, params):
        objectId = params.get('objectId')
        extra = int(params.get('extra', 0))
        try:
            models.ActJoinLog.objects.filter(objectId=objectId).update(
                extra=extra
            )
            return {'code': 0, 'msg': '更新附加费成功'}

        except Exception, e:
            return {'code': 110, 'msg': '不存在该参加活动记录'}
