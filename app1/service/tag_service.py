#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0.1
@author: suyuan
@license: Apache Licence 
@contact: suyuan1573@gmail.com
@site: https://github.com/su6838354/ocp
@software: PyCharm Community Edition
@file: tag_service.py
@time: 2017/3/13 0013 下午 10:49
"""

from app1 import models, util


class TagService(object):
    def __init__(self):
        pass

    def add_update_tag(self, params):
        tag_id = params.get('id')
        txt = params.get('txt')
        if tag_id == 0:
            tag = models.Tag.objects.filter(txt=txt)
            if len(tag) > 0:
                return {'code': 0, 'msg': '重名标签', 'data': {'tag_txt': txt}}
            tag = models.Tag(txt=txt,
                             createdAt=util.get_now_tuc(),
                             updatedAt=util.get_now_tuc())
            tag.save()
            tag_id = tag.id
        else:
            models.Tag.objects.filter(id=tag_id).update(
                txt=txt,
                updatedAt=util.get_now_tuc()
            )
        return {'code': 0, 'msg': '保存成功', 'data': {'id': tag_id}}

    def add_update_activity2tag(self, params):
        a2t_id = params.get('id')
        tag_id = params.get('tag_id')
        activity_id = params.get('activity_id')
        if a2t_id == 0:
            a2t = models.Activity2Tag(activity_id=activity_id,
                                      tag_id=tag_id,
                                      createdAt=util.get_now_tuc(),
                                      updatedAt=util.get_now_tuc())
            a2t.save()
            a2t_id = a2t.id
        else:
            models.Activity2Tag.objects.filter(id=a2t_id).update(
                activity_id=activity_id,
                tag_id=tag_id,
                updatedAt=util.get_now_tuc()
            )
        return {'code': 0, 'msg': '保存成功', 'data': {'id': a2t_id}}

    def delete_activity2tag(self, params):
        a2t_id = params.get('id')
        models.Activity2Tag.objects.filter(id=a2t_id).delete()
        return {'code': 0, 'msg': '删除成功', 'data': {'id': a2t_id}}

    def get_tags(self, params):
        page_index = params.get('page_index', 1)
        limit = params.get('limit', 10)
        txt=params.get('txt', '')
        isDelete=params.get('isDelete', 0)
        tags = models.Tag.objects.filter(isDelete=isDelete, txt__contains=txt).order_by('-createdAt')
        count = tags.count()
        tag_list = tags[(page_index-1)*limit: page_index*limit]
        tag_list = list(tag_list.values())
        res = {'code': 0, 'msg': '获取成功', 'data': tag_list}
        res.update(util.make_pagination(count, page_index, limit))
        return res

    def delete_tags(self, params):
        tag_ids = params.get('tag_ids', [])
        models.Tag.objects.filter(id__in=tag_ids).update(isDelete=1)
        res = {'code': 0, 'msg': '删除成功', 'data': {'tag_ids': tag_ids}}
        return res