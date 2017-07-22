#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: activity_service.py
@time: 2017/3/19 0019 下午 10:30
"""

from app1.services import *


class ActivityService(Services):
    def __init__(self):
        pass

    """
        获取某个活动详情
    """

    def get_activity(self, objectId):
        if objectId:
            activity = models.Activities.objects.get(objectId=objectId)
            activity_dict = model_to_dict(activity)
            tags = models.Activity2Tag.objects.filter(activity_id=activity_dict.get('objectId', 0)).values()
            for tag in tags:
                try:
                    tag['txt'] = models.Tag.objects.get(id=tag.get('tag_id')).txt
                except Exception, e:
                    log.error(e.message)
                    traceback.print_exc()
                    tag['txt'] = ''
            activity_dict['tags'] = list(tags)
            activity_dict['admin'] = model_to_dict(activity.admin)
            return {'code': 0, 'data': activity_dict}
        else:
            return {
                'code': 100,
                'data': {}
            }

    """
    获取活动列表
    """

    def get_activities(self, params):
        isDelete = params.get('isDelete')
        limit = params.get('limit', 10)
        page_index = params.get('page_index', 1)
        group_type = params.get('group_type', 'admin')
        admin_pid = params.get('admin', '')
        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        status = params.get('status', 'pass')
        if group_type == 'admin':
            activities_all = models.Activities.objects.filter(
                Q(isDelete=isDelete),
                Q(admin__pid__contains=admin_pid), q_show
            ).order_by('-createdAt')
        else:
            child_pids = models.Admins.objects.filter(parentId=admin_pid, isDelete=0).values_list('pid', flat=True)
            child_pids = list(child_pids)
            child_pids.append(admin_pid)
            activities_all = models.Activities.objects.filter(
                Q(isDelete=isDelete),
                Q(admin__pid__in=child_pids), q_show
            ).order_by('-createdAt')

        if status != 'all':
            activities_all = activities_all.filter(status=status)

        count = activities_all.count()
        activities = activities_all[(page_index - 1) * limit: page_index * limit]
        owner_fields = [f.name for f in models.Activities._meta.get_fields()]
        owner_fields.remove('actR_user_group')
        owner_fields.remove('actjoinlog')
        fields = owner_fields + ['admin__type', 'admin__objectId', 'admin__name', 'admin__username']
        activities_values = activities.values(*fields)
        for act in activities_values:
            tags = models.Activity2Tag.objects.filter(activity_id=act.get('objectId', 0)).values()
            for tag in tags:
                try:
                    tag['txt'] = models.Tag.objects.get(id=tag.get('tag_id')).txt
                except Exception, e:
                    log.error(e.message)
                    traceback.print_exc()
                    tag['txt'] = ''

            act['tags'] = list(tags)
        res = {'code': 0, 'data': list(activities_values)}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    """
        活动数据导入接口
    """

    def add_activity(self, activity):
        admin_id = activity.get('admin')
        if self.__check_id_tuple(admin_id):
            admin = models.Admins.objects.get(pid=admin_id[0])
            activity['admin'] = admin
        else:
            activity['admin'] = None

        begin = activity.get('begin')
        if begin is not None:
            activity['begin'] = begin.get('ios')

        end = activity.get('end')
        if begin is not None:
            activity['end'] = end.get('ios')

        activity = models.Activities.build(activity)
        activity.save()
        return {'code': 0}

    """
        更新活动
    """

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
            limit=params.get('limit', ''),
            place=params.get('place', ''),
            updatedAt=util.get_now_tuc()
        )
        tag_ids = params.get('tag_ids', [])
        models.Activity2Tag.objects.filter(activity_id=objectId).delete()
        if params.get('isDelete') not in ['1', 1]:
            for tag_id in tag_ids:
                a2t = models.Activity2Tag(activity_id=objectId,
                                          tag_id=tag_id,
                                          createdAt=util.get_now_tuc(),
                                          updatedAt=util.get_now_tuc())
                a2t.save()

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

    """
         创建活动
    """

    def create_activity(self, params):
        params['objectId'] = util.get_uuid_24()
        params['createdAt'] = util.get_now_tuc()
        params['updatedAt'] = util.get_now_tuc()
        params['status'] = 'pass'
        admin_id = params.get('admin')
        if admin_id is not None and admin_id != '':
            admin = models.Admins.objects.get(pid=admin_id)
            params['admin'] = admin
            if admin.group_type == 2:
                "如果是下属单位，默认为待审核"
                params['status'] = 'wait'
        else:
            params['admin'] = None

        activity = models.Activities.build(params)
        activity.save()
        activity_id = activity.objectId
        tag_ids = params.get('tag_ids')
        for tag_id in tag_ids:
            a2t = models.Activity2Tag(activity_id=activity_id,
                                      tag_id=tag_id,
                                      createdAt=util.get_now_tuc(),
                                      updatedAt=util.get_now_tuc())
            a2t.save()
        return {'code': 0, 'data': {'objectId': activity.objectId}, 'msg': '保存成功'}

    """
     获取参加指定活动人数
    """

    def get_act_registration_count(self, params):
        activity_objectId = params.get('activity', '')
        user_pid = params.get('user', '')

        act_registration_count = models.ActRegistration.objects.filter(
            Q(activity=activity_objectId), Q(user__pid__contains=user_pid)
        ).count()
        return {'code': 0, 'data': {'count': act_registration_count}}

    def update_activity_status(self, params):
        objectId = params.get('objectId')
        models.Activities.objects.filter(objectId=objectId).update(
            status=params.get('status')
        )
        return {'code': 0, 'data': {'objectId': objectId}, 'message': '更新状态成功'}
