from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""用户表"""
class Users(models.Model):
    objectId = models.CharField('主键id', max_length=30, unique=True)
    address = models.CharField('地址', max_length=300)
    group = models.ForeignKey('单位', Admin)
    realname = models.CharField('真实姓名', max_length=50)
    sex = models.CharField('性别', max_length=10)
    idcard = models.CharField('身份证号', max_length=30)
    username = models.CharField('用户名', max_length=100)
    checkin = models.CharField('bool,签到日期用，隔开', max_length=300)
    pid = models.CharField('主键', max_length=30, primary_key=True)
    political = models.CharField('党组织身份', max_length=50)
    isShow = models.CharField(max_length=10)
    mobile = models.CharField('手机号码', max_length=30)
    location = models.ForeignKey('居委会', Admin)
    flagNumber = models.CharField('', max_length=20)
    brith = models.DateField('生日，年月日')
    job = models.CharField('职业', max_length=300)
    createdAt = models.DateTimeField('创建时间', )
    updatedAt = models.DateTimeField('更新时间', )

"""单位或者社区表"""
class Admins(models.Model):
    objectId = models.CharField('id', max_length=30, unique=True)
    address = models.CharField('地址', max_length=300)
    person = models.CharField('管理员', max_length=30)
    pwd = models.CharField('密码', max_length=20)
    name = models.CharField('单位组织名称', max_length=200)
    username = models.CharField('用户名', max_length=100)
    type = models.CharField('类别，单位or社区', max_length=30)
    tel = models.CharField('电话号码', max_length=30)
    pid = models.CharField('主键id', max_length=30, primary_key=True)
    isShow = models.CharField(max_length=5)
    mobile = models.CharField(max_length=30)
    flagNumber = models.CharField(max_length=100)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

"""活动表"""
class Activities(models.Model):
    objectId = models.CharField('主键id', max_length=30, primary_key=True)
    limit = models.CharField(max_length=30)
    admin = models.ForeignKey(Admins)
    place = models.CharField(max_length=300)
    content = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    begin = models.DateTimeField()
    idDelete = models.CharField(max_length=10)
    isShow = models.CharField(max_length=10)
    joinnum = models.IntegerField()
    end = models.DateTimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

"""活动参加信息表"""
class ActRegistration(models.Model):
    objectId = models.CharField(max_length=30, primary_key=True)
    admin = models.ForeignKey('活动具体组织 group', Admins)
    userLocationArr = models.ForeignKey('加入活动的人所在社区', Admins)
    activity = models.ForeignKey('活动', Activities)
    isInner = models.BooleanField()
    userGroupArr = models.ForeignKey('加入活动的人所在单位', Admins)
    user = models.ForeignKey(Users)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

class ActJoinLog(models.Model):
    objectId = models.CharField(max_length=30, primary_key=True)
    admin = models.ForeignKey(Admins)
    userLocationArr = models.ForeignKey(Admins)
    extra = models.IntegerField()
    star = models.IntegerField()
    activity = models.ForeignKey(Activities)
    isInner = models.BooleanField()
    userGroupArr = models.ForeignKey(Admins)
    user = models.ForeignKey(Users)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()




















