#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: admin_service.py
@time: 2017/3/19 0019 下午 9:54
"""

from app1.services import *


class AdminService(Services):
    def __init__(self):
        pass

    def add_admin(self, admin):
        admin = models.Admins.build(admins=admin)
        admin.save()
        return {'code': 0}

    def get_admins(self, params):
        limit = params.get('limit', 10)
        page_index = params.get('page_index', 1)
        q_list = []

        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        q_list.append(q_show)

        type = params.get('type')
        if type is not None:
            q_list.append(Q(type=type))

        username = params.get('username', '')
        if username != '':
            q_list.append(Q(username__contains=username))

        name = params.get('name', '')
        if name != '':
            q_list.append(Q(name__contains=name))

        parentId = params.get('parentId')
        if parentId is not None:
            q_list.append(Q(parentId=parentId))

        group_type = params.get('group_type')
        if group_type is not None:
            q_list.append(Q(group_type=group_type))

        q_list.append(Q(isDelete=0))
        admins_all = models.Admins.objects.filter(
            *q_list
            # q_show,
            # Q(name__contains=name),
            # Q(username__contains=username),
            # Q(type=type)
        ).order_by('-createdAt')
        count = admins_all.count()
        admins = admins_all[(page_index - 1) * limit: page_index * limit]
	log.info(admins)
        # admins_json = serializers.serialize('json', admins)
	log.info(1)
        fields = [f.name for f in models.Admins._meta.fields]
        # fields.append('')
        admins_list = list(admins.values(*fields))
	log.info(2);
        res = {'code': 0, 'data': admins_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def get_admin(self, params):
        pid = params.get('pid')
        admin = models.Admins.objects.get(pid=pid)
        admin_dict = model_to_dict(admin)
        return {'code': 0, 'data': admin_dict}

    def update_admin(self, params):
        pid = params.get('pid', '')
        models.Admins.objects.filter(pid=pid).update(
            address=params.get('address', ''),
            person=params.get('person',  ''),
            name=params.get('name'),
            username=params.get('username', ''),
            tel=params.get('tel', ''),
            isShow=params.get('isShow', 1),
            mobile=params.get('mobile', ''),
            flagNumber=params.get('flagNumber', ''),
            group_type=params.get('group_type', 0),
            parentId=params.get('parentId', ''),
            updatedAt=util.get_now_tuc()
        )
        return {'code': 0, 'data': {'pid': pid}, 'msg': '更新成功'}

    def delete_admin(self, params):
        pid = params.get('pid', '')
        models.Admins.objects.filter(pid=pid).update(isDelete=1)
        return {'code': 0, 'msg': '删除成功', 'data': {'pid': pid}}
