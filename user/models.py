from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# Create your models here.


class User(AbstractUser,BaseModel):

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name  



class AddressManager(models.Manager):
    '''地址模型管理器类'''
    # 自定义模型管理器的两种应用场景​
    # 1. 改变原有查询结果集​: all()
    # 2. ​封装方法: 用户操作模型类对应的数据表(增删改查)
    def get_default_address(self, user):
        '''获取用户默认的收货地址'''
        # self.model: 获取self对象所在的模型类​
        try:
            address = self.get(user=user, is_default=True)  # objects, django给每一个类生成的管理器对象: 默认models.Manager
        except self.model.DoesNotExist:
            # 不存在默认收货地址
            address = None

        return address


class Address(BaseModel):
    '''地址模型类'''
    user = models.ForeignKey('User',on_delete=models.CASCADE, verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    # default=False, default表示是否默认, False设置默认不是一个默认的
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器对象
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
