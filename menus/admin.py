from django.contrib import admin

from menus import models
# Register your models here.

admin.site.register(models.Menu)
admin.site.register(models.MenuTypes)
admin.site.register(models.MenuTypeItem)