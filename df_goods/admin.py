# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from df_goods.models import TypeInfo,GoodsInfo


# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    # list_display = ['id','gtitle','gprice','gunit','gkucun','gcontent','gtype']
    list_display = ['id','gtitle','gprice','gunit','gkucun','gtype']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)