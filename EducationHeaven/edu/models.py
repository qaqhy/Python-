from django.db import models


# Create your models here.
class Admin(models.Model):
    aid = models.AutoField()  # 管理员id
    nickname = models.CharField(max_length=8, unique=True)  # 管理员昵称长度限制为8位
    position = models.CharField(max_length=8, blank=True)  # 管理员职位
    phone = models.CharField(max_length=11, unique=True)  # 联系电话
    mail = models.EmailField()  # 管理员邮箱
    password = models.CharField(max_length=16)  # 管理员密码


class Developer(models.Model):
    did = models.AutoField()  # 开发者id
    name = models.CharField(max_length=8)  # 开发者名字
    phone = models.CharField(max_length=11, unique=True)  # 联系电话
    mail = models.EmailField()  # 管理员邮箱
    password = models.CharField(max_length=16)  # 密码


class Channel(models.Model):
    """公司、培训机构、学校、个人工作室"""
    cid = models.AutoField()  # 渠道id
    name = models.CharField(max_length=8, unique=True)  # 公司名
    phone = models.CharField(max_length=11)  # 公司电话
    mail = models.EmailField()  # 公司邮箱
    password = models.CharField(max_length=16)  # 密码
    address = models.CharField(max_length=16)  # 公司地址
    rmb = models.IntegerField()  # 公司人民币余额
    eb = models.IntegerField()  # 公司E币余额


class Resource(models.Model):
    """公司、培训机构、学校、个人工作室"""
    rid = models.AutoField()  # 资源id
    cid = models.ForeignKey('Channel', on_delete=models.CASCADE)  # 渠道id
    aid = models.ForeignKey('Admin', on_delete=models.CASCADE)  # 管理员id
    jurisdiction = models.CharField(max_length=8)  # 权限
    description = models.CharField(max_length=256)  # 资源说明
    address = models.CharField(max_length=128)  # 资源地址
    price = models.CharField(max_length=16, default='0E')  # 价格
    title = models.CharField(max_length=16)  # 标题
    enter_date = models.DateField()  # 录入日期
    pass_date = models.DateField()  # 通过日期
    view_count = models.IntegerField()  # 观看量
    password = models.CharField(max_length=16)  # 密码
