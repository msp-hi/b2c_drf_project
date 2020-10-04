'''
Author: your name
Date: 2020-10-02 09:32:07
LastEditTime: 2020-10-04 12:28:41
LastEditors: your name
Description: In User Settings Edit
FilePath: \b2c_drf_project\goods\admin.py
'''
from django.contrib import admin

# Register your models here.
from goods.models import GoodsType, GoodsTypeMenu


admin.site.register(GoodsType)
admin.site.register(GoodsTypeMenu)