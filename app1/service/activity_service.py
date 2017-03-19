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

    def get_activities(self, params):
        isDelete = params.get('isDelete')
        limit = params.get('limit', 10)
        page_index = params.get('page_index', 1)
        type = params.get('type', 'admin')
        admin_pid = params.get('admin', '')
        isShow = params.get('isShow', '-1')
        q_show = self._get_q_show(isShow)
        if type == 'admin':
            activities_all = models.Activities.objects.filter(
                Q(isDelete=isDelete),
                Q(admin__pid__contains=admin_pid), q_show
            ).order_by('-createdAt')
        else:
            child_pids = models.Admins.objects.filter(parentId=admin_pid).values_list('pid', flat=True)
            child_pids = list(child_pids)
            child_pids.append(admin_pid)
            activities_all = models.Activities.objects.filter(
                Q(isDelete=isDelete),
                Q(admin__pid__in=child_pids), q_show
            ).order_by('-createdAt')

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