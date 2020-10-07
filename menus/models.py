from django.db import models

# Create your models here.


class Menu(models.Model):
    '''一级菜单'''
    name = models.CharField(verbose_name='一级菜单名称', max_length=32) 
    icon = models.CharField(verbose_name='图标', max_length=32, null=True, blank=True)
    url = models.CharField(max_length=128, verbose_name='URL')
    component = models.CharField(max_length=20, verbose_name='组件名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drf_menu'
        verbose_name = '一级菜单'
        verbose_name_plural = verbose_name


class MenuTypes (models.Model):
    '''二级菜单'''
    types = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='所属菜单')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    url = models.CharField(max_length=128, verbose_name='URL')
    component = models.CharField(max_length=20, verbose_name='组件名称', blank=True,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drf_menu_type'
        verbose_name = '二级菜单'
        verbose_name_plural = verbose_name

    


class MenuTypeItem(models.Model):
    '''三级菜单'''
    types = models.ForeignKey('MenuTypes', on_delete=models.CASCADE, verbose_name='所属二级菜单')
    # image = models.ImageField(upload_to='menuclass', verbose_name='标识图')
    image = models.CharField(max_length=128, verbose_name='标识图')
    name = models.CharField(max_length=20, verbose_name='种类名称')
    url = models.CharField(verbose_name='URL', max_length=128)
    component = models.CharField(max_length=20, verbose_name='组件名称', blank=True,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drf_menu_type_item'
        verbose_name = '三级菜单'
        verbose_name_plural = verbose_name

