# -*- coding: utf-8 -*-
from django.contrib import admin
from zen.customer.models import Customer, CustomerMemo

class MemoInline(admin.TablularInline):
    model = CustomerMemo
    extra = 2

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None',    {'fields': ['sei', 'mei', 'kanasei', 'kanamei',
                                'pref', 'add1', 'add2', 
                                'tel1', 'tel1_is_mobile',
                                'email1', 'email1_is_mobile']}),
        (u'è⁄ç◊',   {'fields': ['tel2', 'tel2_is_mobile',
                                'email2', 'email2_is_mobile',
                                'sex', 'age',
                                'birthday',
                                'first_contact', 'first_buy'],
                     'clases': ['collapse']}),
    ]
    inlines = [MemoInline]
    list_display = ('sei', 'mei', 'pref', 'add1', 'tel1')
                                

admin.site.register(Customer, CustomerAdmin)
