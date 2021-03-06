# Generated by Django 2.2.16 on 2020-10-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updeate_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
                'db_table': 'df_goods_type',
            },
        ),
        migrations.CreateModel(
            name='GoodsTypeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updeate_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='种类名称')),
                ('url', models.CharField(max_length=128, verbose_name='URL')),
                ('image', models.ImageField(upload_to='type', verbose_name='商品种类图')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='所属商品类型')),
            ],
            options={
                'verbose_name': '商品种类',
                'verbose_name_plural': '商品种类',
                'db_table': 'df_goods_Menu',
            },
        ),
    ]
