#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: user_service.py
@time: 2017/3/19 0019 下午 9:55
"""

from app1.services import *


class UserService(Services):
    def __init__(self):
        pass

    def get_users(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        order_by = params.get('order_by', 'flagNumber')
        q_list = []

        checkin = params.get('checkin')
        if checkin is not None:
            if checkin is False:
                q_list.append(Q(checkin=None))
            else:
                q_list.append(~Q(checkin=None))

        group = params.get('group', '')
        if group != '':
            group_type = params.get('group_type', 'admin')
            if group_type == 'admin':
                    q_list.append(Q(group__pid__contains=group))
            elif group_type == 'all':
                child_pids = models.Admins.objects.filter(parentId=group, isDelete=0).values_list('pid', flat=True)
                child_pids = list(child_pids)
                child_pids.append(group)
                q_list.append(Q(group__pid__in=child_pids))
            else:
                pass

        group__name = params.get('group__name', '')
        if group__name != '':
            q_list.append(Q(group__name__contains=group__name))

        location = params.get('location', '')
        if location != '':
            q_list.append(Q(location__pid__contains=location))

        location__name = params.get('location__name', '')
        if location__name != '':
            q_list.append(Q(location__name__contains=location__name))

        flagNumber = params.get('flagNumber', '')
        if flagNumber != '':
            q_list.append(Q(flagNumber__contains=flagNumber))

        mobile = params.get('mobile', '')
        if mobile != '':
            q_list.append(Q(mobile__contains=mobile))
        idcard = params.get('idcard', '')
        if idcard != '':
            q_list.append(Q(idcard__contains=idcard))

        realname = params.get('realname', '')
        if realname != '':
            q_list.append(Q(realname__contains=realname))

        username = params.get('username', '')
        if username != '':
            q_list.append(Q(username__contains=username))

        political = params.get('political', '')
        if political != '':
            q_list.append(Q(political__contains=political))

        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        q_list.append(q_show)
        q_list.append(Q(isDelete=0))
        users = models.Users.objects.filter(
            *q_list
            #            Q(group__pid__contains=group), Q(flagNumber__contains=flagNumber),
            #            Q(mobile__contains=mobile), Q(idcard__contains=idcard),
            #            Q(realname__contains=realname), Q(username__contains=username),
            #            Q(location__pid__contains=location),
            #            q_show
        ).order_by(order_by)
        count = users.count()
        fields = [f.name for f in models.Users._meta.fields]
        other_fields = ['group__pid', 'group__address', 'group__name', 'group__username', 'location__pid',
                        'location__address', 'location__name', 'location__username']
        fields.extend(other_fields)
        users_list = list(users.values(*fields)[(page_index - 1) * limit: page_index * limit])
        res = {'code': 0, 'data': users_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def delete_user(self, params):
        pid = params.get('pid', '')
        models.Users.objects.filter(pid=pid).update(isDelete=1)
        return {'code': 0, 'msg': '删除成功', 'data': {'pid': pid}}
