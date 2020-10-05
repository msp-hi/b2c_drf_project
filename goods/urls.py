from django.urls import path
from goods import views

urlpatterns = [
    path('goodstype/list', views.GoodsTypeList.as_view(), name='goodstype-list'),
    path('goodsclass/list', views.GoodsTypeMenuList.as_view(), name='goodsclass-list'),
]