# b2c_drf_project

## menus
> 用于实现网站菜单应用

### 模型类设计
- 一级菜单
    - name 名称
    - icon 图标
    - url  地址
    - component 组件
- 二级菜单
    - type 所属菜单
    - name 名称
    - url  地址
    - component 组件
- 三级菜单
    - types 所属二级菜单
    - image 标识图
    - name 名称
    - url  地址
    - component 组件


### 首页一级菜单api
http://127.0.0.1:8000/menus/menu/list

### 首页二级菜单api
http://127.0.0.1:8000/menus/menutype/list/1

### 首页三级菜单api
http://127.0.0.1:8000/menus/menuitem/list/1
http://127.0.0.1:8000/menus/menuitem/list/3

### 社区的二级菜单api
http://127.0.0.1:8000/menus/menutype/list/3

### 社区的三级菜单api
http://127.0.0.1:8000/menus/menuitem/list/7
