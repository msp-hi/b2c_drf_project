from db.base_model import BaseModel
from django.db import models

# Create your models here.


class GoodsType (BaseModel):
    '''商品类型模型类'''
    name = models.CharField(max_length=20, verbose_name='种类名称')
    # logo是雪碧图,通过不同的类显示不同的位置, 数据库保存它的类名
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='商品类型图')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标准产品单位, 产品名称和介绍可复用
class Goods(BaseModel):
    '''商品SPU模型类'''
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    detail = models.CharField(max_length=256, blank=True, verbose_name='商品详情')    

    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name


# 商品详情
class GoodsSKU(models.Model):
    '''商品SKU模型类'''
    type = models.ForeignKey('GoodsType', on_delete=models.CASCADE, verbose_name='商品种类')
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name='商品SPU')
    name = models.CharField(max_length=20, verbose_name='商品名称')
    desc = models.CharField(max_length=256,verbose_name='商品简介')
    # max_digits：数字允许的最大位数, decimal_places=2：小数的最大位数,保留两位小数
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='商品价格')
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    image = models.ImageField(upload_to='goods', verbose_name='商品图片')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')

    class Meta:
        db_table = 'df_goods_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name



class GoodsImage(BaseModel):
    '''商品图片模型类'''
    sku = models.ForeignKey('GoodsSKU',on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField(upload_to='goods', verbose_name='图片路径')

    class Meta:
        db_table = 'df_goods_image'
        verbose_name = '商品图品'
        verbose_name_plural = verbose_name


class IndexGoodsBanned(BaseModel):
    '''首页轮播商品展示模型类'''
    sku = models.ForeignKey('GoodsSKU', on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name


class IndexTypeGoodsBanner(BaseModel):
    '''首页分类商品展示模型类'''
    DISPLAY_TYPE_CHOICES = (
        (0,'标题'),
        (1,'图片'),
    )

    type = models.ForeignKey('GoodsType', on_delete=models.CASCADE ,verbose_name='商品类型')
    sku = models.ForeignKey('GoodsSKU', on_delete=models.CASCADE, verbose_name='商品SKU')
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_type_banner'
        verbose_name = '首页分类商品展示'
        verbose_name_plural = verbose_name


class IndexPromotionBanner(BaseModel):
    '''首页促销活动模型类'''
    name = models.CharField(max_length=20, verbose_name='活动名称')
    # url = models.URLField(verbose_name='活动链接')    # URLField: 用来存放url链接的字段类型
    url = models.CharField(max_length=256, verbose_name='活动链接')    # URLField: 用来存放url链接的字段类型
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = '主页促销活动'
        verbose_name_plural = verbose_name

