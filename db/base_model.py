'''
Author: your name
Date: 2020-10-03 10:56:07
LastEditTime: 2020-10-03 11:03:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \b2c_drf_project\db\base_model.py
'''
from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updeate_time = models .DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        abstract = True
 