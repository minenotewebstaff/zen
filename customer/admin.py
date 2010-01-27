# -*- coding: utf-8 -*-
from django.contrib import admin
from zen.customer.models import *

class MemoInline(admin.TabularInline):
    model = CustomerMemo
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None',    {'fields': ['sei', 'mei', 'kanasei', 'kanamei',
                                'zip', 'pref', 'add1', 'add2', 
                                'tel1', 'tel1_is_mobile',
                                'email1', 'email1_is_mobile']}),
        (u'詳細',   {'fields': ['tel2', 'tel2_is_mobile',
                                'email2', 'email2_is_mobile',
                                'sex', 'age',
                                'birthday',
                                'first_contact', 'first_buy'],
                     'classes': ['collapse']}),
    ]
    inlines = [MemoInline]
    #list_display = ('sei', 'mei', 'pref', 'add1', 'tel1')




class SalesDatailInline(admin.TabularInline):
    model = SalesDetail
    extra = 1

class SalesSlipAdmin(admin.ModelAdmin):
    inlines = [SalesDatailInline]
    
class SizeAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass
  
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(SalesSlip, SalesSlipAdmin)


