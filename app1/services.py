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
        page_index = params.get('page_index')
        admins_all = models.Admins.objects.filter(Q(isShow=isShow))
        count = admins_all.count()
        admins = admins_all[(page_index - 1) * limit: page_index * limit]
        # admins_json = serializers.serialize('json', admins)
        admins_list = list(admins.values())
        res = {'code': 0, 'data': admins_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def get_admin(self, params):
        pid = params.get('pid')
        admin = models.Admins.objects.get(pid=pid)
        admin_dict = model_to_dict(admin)
        return {'code': 0, 'data': admin_dict}

    def update_admin(self, params):
        params['updatedAt'] = util.get_now_tuc()
        admin = models.Admins.build(admins=params)
        admin.save()
        return {'code': 0, 'data': {'pid': admin.pid}, 'msg': '更新成功'}

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

    def update_user_checkin(self, params):
        user = params.get('user', '')
        checkin = params.get('checkin')
        if checkin:
            checkin = json.dumps(checkin)
            checkin = checkin
        else:
            checkin = None

        models.Users.objects.filter(pid=user).update(
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

        user = models.Users.build(user)
        user.save()
        return {'code': 0, 'msg': '更新成功', 'data': {'pid': user.pid}}

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

    def get_users(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        order_by = params.get('order_by', 'flagNumber')
        group = params.get('group', '')
        flagNumber = params.get('flagNumber')
        mobile=params.get('mobile', '')
        idcard=params.get('idcard', '')
        realname=params.get('realname', '')
        username=params.get('username', '')
        users = models.Users.objects.filter(
            Q(group__pid__contains=group), Q(flagNumber__contains=flagNumber),
            Q(mobile__contains=mobile), Q(idcard__contains=idcard),
            Q(realname__contains=realname), Q(username__contains=username)
        ).order_by(order_by)
        count = users.count()
        users_list = list(users.values()[(page_index-1)*limit: page_index*limit])
        res = {'code': 0, 'data': users_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res


    def get_user_checkin(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        checkin = params.get('checkin')
        group = params.get('group', '')
        if checkin is False:
            users = models.Users.objects.filter(
                Q(checkin=None), Q(group__pid__contains=group)
            )
        else:
            users = models.Users.objects.filter(
                ~Q(checkin=None), Q(group__pid__contains=group)
            )
        count = users.count()
        users_list = list(users[(page_index-1)*limit: page_index*limit].values())
        res = {'code': 0, 'data': users_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res


    def get_activity(self, objectId):
        if objectId:
            activity = models.Activities.objects.get(objectId=objectId)
            activity_dict = model_to_dict(activity)
            activity_dict['admin'] = model_to_dict(activity.admin)
            return {'code': 0, 'data': activity_dict}
        else:
            return {'code': 100, 'data': {}}

    def update_activity(self, params):
        # params['objectId'] = util.get_uuid_24()
        # params['createdAt'] = util.get_now_tuc()
        objectId = params.get('objectId')
        models.Activities.objects. \
            filter(objectId=objectId).update(
            content=params.get('content'),
            title=params.get('title'),
            isDelete=params.get('isDelete'),
            isShow=params.get('isShow'),
            updatedAt=util.get_now_tuc()
        )
        return {'code': 0, 'data': {'objectId': objectId}, 'msg': '更新成功'}

        #
        # params['updatedAt'] = util.get_now_tuc()
        #
        # admin_id = params.get('admin')
        # if admin_id is not None and admin_id != '':
        #     admin = models.Admins.objects.get(pid=admin_id)
        #     params['admin'] = admin
        # else:
        #     params['admin'] = None
        # activity = models.Activities.build(params)
        # activity.save()

    def get_activities(self, params):
        isDelete = params.get('isDelete')
        isShow = params.get('isShow')
        limit = params.get('limit')
        page_index = params.get('page_index')
        admin_pid = params.get('admin', '')
        activities_all = models.Activities.objects.filter(
            Q(isDelete=isDelete), Q(isShow=isShow), Q(admin__pid__contains=admin_pid)
        ).order_by('-createdAt')
        count = activities_all.count()
        activities = activities_all[(page_index - 1) * limit: page_index * limit]
        owner_fields = [f.name for f in models.Activities._meta.get_fields()]
        owner_fields.remove('actR_user_group')
        owner_fields.remove('actjoinlog')
        fields = owner_fields + ['admin__type', 'admin__objectId', 'admin__name', 'admin__username']
        activities_values = activities.values(*fields)
        res = {'code': 0, 'data': list(activities_values)}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def get_activities_by_join(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        join = params.get('join', False)
        admin = params.get('admin')
        user = params.get('user')
        join_activities = models.ActJoinLog.objects.filter(
            Q(admin__pid=admin), Q(user__pid=user)
        ).values_list('activity__objectId', flat=True).distinct()
        if join is False:
            activities = models.Activities.objects.filter(admin__pid=admin).exclude(
                objectId__in=join_activities
            )
        else:
            activities = models.Activities.objects\
                .filter(admin__pid=admin, objectId__in=join_activities
            )
        count = activities.count()
        res = {'code': 0, 'data': list(activities.values())}
        res.update(util.make_pagination(count, page_index, limit))
        return res

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

    def get_act_registration_count(self, params):
        activity_objectId = params.get('activity', '')
        user_pid = params.get('user', '')
        act_registration_count = models.ActRegistration.objects.filter(
            Q(activity=activity_objectId), Q(user__pid__contains=user_pid)
        ).count()
        return {'code': 0, 'data': {'count': act_registration_count}}

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
        user_id = params.get('user')
        admin_id = params.get('admin', '')
	activity_id = params.get('activity', '')
        act_join_logs = models.ActJoinLog.objects.filter(
            Q(user__pid__contains=user_id),
            Q(admin__pid__contains=admin_id),
	    Q(activity__objectId__contains=activity_id)
        ).order_by('-createdAt')
        count = act_join_logs.count()
        act_join_logs_values = act_join_logs[(page_index-1)*limit: page_index*limit].values()
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
            joinnum=F('joinnum')+1
        )
        util.log.info('act_join_id:%s join activity_id:%s' % (act_registeration.objectId, activity_id))
        return {'code': 0, 'data': {'objectId': act_registeration.objectId}, 'msg': 'save success'}
