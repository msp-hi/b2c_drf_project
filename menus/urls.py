from django.urls import path
from menus import views

urlpatterns = [
    path('menu/list', views.MenuList.as_view(), name='menu-list'),
    path('menutpye/list/<int:pk>', views.MenuTypeList.as_view(), name='menutype-list'),
    path('menuitem/list/<int:pk>', views.MenuTypeItemList.as_view(), name='menuitem-list'),
]