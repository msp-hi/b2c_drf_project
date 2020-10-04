'''
Author: your name
Date: 2020-10-02 09:32:07
LastEditTime: 2020-10-04 12:25:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \b2c_drf_project\goods\models.py
'''
from db.base_model import BaseModel
from django.db import models

# Create your models here.


class GoodsType (BaseModel):
    '''商品类型模型类'''
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsTypeMenu (BaseModel):
    '''商品种类模型类'''
    type = models.ForeignKey('GoodsType', on_delete=models.CASCADE, verbose_name='所属商品类型')
    name = models.CharField(max_length=20, verbose_name='种类名称')
    url = models.CharField(verbose_name='URL', max_length=128)
    image = models.ImageField(upload_to='type', verbose_name='商品种类图')

    class Meta:
        db_table = 'df_goods_Menu'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


