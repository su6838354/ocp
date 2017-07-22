#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class _User(models.Model):
    objectId = models.CharField('主键', max_length=30, primary_key=True)
    salt = models.CharField(max_length=100, default='', null=True)
    email = models.CharField(max_length=100, default='', null=True)
    sessionToken = models.CharField(max_length=100, default='', null=True)
    password = models.CharField(max_length=200, default='', null=True)
    username = models.CharField(max_length=30, default='', null=True)
    emailVerified = models.BooleanField(default=False)
    mobilePhoneNumber = models.CharField(max_length=30, default='', null=True)
    authData = models.CharField(max_length=100, default='', null=True)
    userRole = models.CharField(max_length=20, default='', null=True)
    mobilePhoneVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)

    @staticmethod
    def build(_user):
        _user = _User(objectId=_user.get('objectId'),
                      salt=_user.get('salt', ''),
                      email=_user.get('email', ''),
                      sessionToken=_user.get('sessionToken', ''),
                      password=_user.get('password', ''),
                      username=_user.get('username', ''),
                      emailVerified=_user.get('emailVerified', False),
                      mobilePhoneNumber=_user.get('mobilePhoneNumber', ''),
                      authData=_user.get('authData', ''),
                      userRole=_user.get('userRole', ''),
                      mobilePhoneVerified=_user.get('mobilePhoneVerified', False),
                      createdAt=_user.get('createdAt'),
                      updatedAt=_user.get('updatedAt')
                      )
        return _user



"""用户表"""
class Users(models.Model):
    objectId = models.CharField('主键id', max_length=30, unique=True)
    address = models.CharField('地址', max_length=300, default='', null=True)
    group = models.ForeignKey('Admins', related_name='user_group', null=True)
    realname = models.CharField('真实姓名', max_length=50, default='', null=True)
    sex = models.CharField('性别', max_length=10, null=True)
    idcard = models.CharField('身份证号', max_length=30, default='', null=True)
    username = models.CharField('用户名', max_length=100, default='', null=True)
    checkin = models.CharField('bool,签到日期用，隔开', max_length=300, null=True)
    checkin2016 = models.CharField('bool,2016签到日期用，隔开', max_length=300, null=True)
    pid = models.CharField('主键对应到_user中', max_length=30, primary_key=True)
    political = models.CharField('党组织身份', max_length=50, default='', null=True)
    isShow = models.CharField(max_length=10, default='', null=True)
    mobile = models.CharField('手机号码', max_length=30, default='', null=True)
    location = models.ForeignKey('Admins', related_name='user_location', null=True)
    flagNumber = models.CharField('flagNumber', max_length=20, default='', null=True)
    birth = models.DateTimeField('生日，年月日', null=True)
    job = models.CharField('职业', max_length=300, default='', null=True)
    createdAt = models.DateTimeField('创建时间', null=True)
    updatedAt = models.DateTimeField('更新时间', null=True)
    isDelete = models.IntegerField(default=0)

    @staticmethod
    def build(user):
        user = Users(objectId=user.get('objectId'),
                     address=user.get('address'),
                     group=user.get('group'),
                     realname=user.get('realname'),
                     sex=user.get('sex'),
                     idcard=user.get('idcard'),
                     username=user.get('username'),
                     checkin=user.get('checkin'),
                     pid=user.get('pid'),
                     political=user.get('political'),
                     isShow=user.get('isShow'),
                     mobile=user.get('mobile'),
                     location=user.get('location'),
                     flagNumber=user.get('flagNumber'),
                     birth=user.get('birth'),
                     job=user.get('job'),
                     createdAt=user.get('createdAt'),
                     updatedAt=user.get('updatedAt'),
                     isDelete=user.get('isDelete', 0)
                     )
        return user

"""单位或者社区表"""
class Admins(models.Model):
    objectId = models.CharField('id', max_length=30, unique=True)
    address = models.CharField('地址', max_length=300, default='', null=True)
    person = models.CharField('管理员', max_length=30, default='', null=True)
    pwd = models.CharField('密码', max_length=20, default='', null=True)
    name = models.CharField('单位组织名称', max_length=200, default='', null=True)
    username = models.CharField('用户名', max_length=100, default='', null=True)
    type = models.CharField('类别，单位or社区', max_length=30, default='', null=True)
    tel = models.CharField('电话号码', max_length=30, default='', null=True)
    pid = models.CharField('主键id', max_length=30, primary_key=True)
    isShow = models.CharField(max_length=5, default='', null=True)
    mobile = models.CharField(max_length=30, default='', null=True)
    flagNumber = models.CharField(max_length=100, default='', null=True)
    group_type = models.IntegerField(default=0)
    parentId = models.CharField(max_length=30, default='')
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)
    isDelete = models.IntegerField(default=0)

    @staticmethod
    def build(admins):
        return Admins(objectId=admins.get('objectId'),
                      address=admins.get('address'),
                      person=admins.get('person'),
                      pwd=admins.get('pwd'),
                      name=admins.get('name'),
                      username=admins.get('username'),
                      type=admins.get('type'),
                      tel=admins.get('tel'),
                      pid=admins.get('pid'),
                      isShow=admins.get('isShow'),
                      mobile=admins.get('mobile'),
                      flagNumber=admins.get('flagNumber', ''),
                      group_type=admins.get('group_type', 0),
                      parentId=admins.get('parentId', ''),
                      createdAt=admins.get('createdAt'),
                      updatedAt=admins.get('updatedAt'),
                      isDelete=admins.get('isDelete', 0)
                      )


"""活动表"""
class Activities(models.Model):
    objectId = models.CharField('主键id', max_length=30, primary_key=True)
    limit = models.CharField(max_length=30, null=True)
    admin = models.ForeignKey(Admins, null=True)
    place = models.CharField(max_length=300, null=True)
    content = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=100, null=True)
    begin = models.DateTimeField(null=True)
    isDelete = models.CharField(max_length=10, null=True)
    isShow = models.CharField(max_length=10, null=True)
    joinnum = models.IntegerField(null=True)
    end = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, null=True, default='pass')

    @staticmethod
    def build(activities):
        return Activities(objectId=activities.get('objectId'),
                          limit=activities.get('limit'),
                          admin=activities.get('admin'),
                          place=activities.get('place'),
                          content=activities.get('content'),
                          title=activities.get('title'),
                          begin=activities.get('begin'),
                          isDelete=activities.get('isDelete'),
                          isShow=activities.get('isShow'),
                          joinnum=activities.get('joinnum'),
                          end=activities.get('end'),
                          createdAt=activities.get('createdAt'),
                          updatedAt=activities.get('updatedAt'),
                          status=activities.get('status')
                          )


"""活动参加信息表"""
class ActRegistration(models.Model):
    objectId = models.CharField(max_length=30, primary_key=True)
    admin = models.ForeignKey(Admins, related_name='actR_admin_group', null=True)
    userLocationArr = models.ForeignKey(Admins, related_name='actR_user_group', null=True)
    activity = models.ForeignKey(Activities, related_name='actR_user_group', null=True)
    isInner = models.BooleanField(default=True)
    userGroupArr = models.ForeignKey(Admins, related_name='actR_user_location', null=True)
    user = models.ForeignKey(Users, null=True)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)

    @staticmethod
    def build(act_registration):
        act_registration = ActRegistration(objectId=act_registration.get('objectId'),
                                           admin=act_registration.get('admin'),
                                           userLocationArr=act_registration.get('userLocationArr'),
                                           activity=act_registration.get('activity'),
                                           isInner=act_registration.get('isInner'),
                                           userGroupArr=act_registration.get('userGroupArr'),
                                           user=act_registration.get('user'),
                                           createdAt=act_registration.get('createdAt'),
                                           updatedAt=act_registration.get('updatedAt')
                                           )
        return act_registration


class ActJoinLog(models.Model):
    objectId = models.CharField(max_length=30, primary_key=True)
    admin = models.ForeignKey(Admins, related_name='actJL_admin_group', null=True)
    userLocationArr = models.ForeignKey(Admins, related_name='actJL_user_location', null=True)
    extra = models.IntegerField(null=True)
    star = models.IntegerField(null=True)
    mark = models.IntegerField(null=True)
    activity = models.ForeignKey(Activities, null=True)
    isInner = models.BooleanField(default=False)
    userGroupArr = models.ForeignKey(Admins, related_name='actJL_user_group', null=True)
    user = models.ForeignKey(Users, null=True)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)

    @staticmethod
    def build(act_join_log):
        act_join_log = ActJoinLog(objectId=act_join_log.get('objectId'),
                                  admin=act_join_log.get('admin'),
                                  userLocationArr=act_join_log.get('userLocationArr'),
                                  extra=act_join_log.get('extra'),
                                  star=act_join_log.get('star'),
                                  mark=act_join_log.get('mark'),
                                  activity=act_join_log.get('activity'),
                                  isInner=act_join_log.get('isInner'),
                                  userGroupArr=act_join_log.get('userGroupArr'),
                                  user=act_join_log.get('user'),
                                  createdAt=act_join_log.get('createdAt'),
                                  updatedAt=act_join_log.get('updatedAt')
                                  )
        return act_join_log


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    txt = models.CharField(max_length=300, null=True)
    isDelete = models.IntegerField(default=0)
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)


class Activity2Tag(models.Model):
    id = models.AutoField(primary_key=True)
    activity_id = models.CharField(max_length=30)
    tag_id = models.IntegerField()
    createdAt = models.DateTimeField(null=True)
    updatedAt = models.DateTimeField(null=True)



















