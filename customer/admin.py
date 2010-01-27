# -*- coding: utf-8 -*-
from django.contrib import admin
from zen.customer.models import Customer, CustomerMemo

admin.site.register(Customer)
admin.site.register(CustomerMemo)
