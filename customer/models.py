# -*- coding: utf-8 -*-
from django.db import models
from datetime import date

# Create your models here.
class Customer(models.Model):
    SEX_CHOICES = (
        ('M', u'男性'),
        ('F', u'女性'),
    )
    code = models.CharField(u'顧客コード', max_length=256, unique = True)
    sei  = models.CharField(u'姓', max_length=100)
    mei  = models.CharField(u'名', max_length=100)
    sex  = models.CharField(u'性別', max_length=1, choices=SEX_CHOICES)
    zip  = models.CharField(u'郵便番号', max_length=7)
    pref = models.CharField(u'都道府県', max_length=20)
    add1 = models.CharField(u'住所1', max_length=256)
    add2 = models.CharField(u'住所2', max_length=256, blank=True)
    tel  = models.CharField(u'TEL', max_length= 20)
    mobile = models.CharField(u'携帯電話', max_length = 20, blank=True)
    email = models.CharField(u'email', max_length=100)
    mobilemail = models.CharField(u'携帯メール', max_length=100, blank=True)
    birthday = models.DateField(u'生年月日', null=True, blank=True)
    first_contact = models.DateField(u'初回接触', null=True, blank=True)
    first_buy = models.DateField(u'初回購入日', null=True, blank=True)
    memo = models.TextField(u'メモ', blank=True)
    
    def __unicode__(self):
        return self.code
    
    class Meta:
        db_table = 'customer'

class CustomerMemo(models.Model):
    customer = models.ForeignKey(Customer)
    memo_date = models.DateField(u'メモ追加日', default=date.today())
    subject = models.CharField(u'メモタイトル', max_length=100)
    memo = models.TextField(u'追加顧客メモ')

    def __unicode__(self):
        return self.subject

    class Meta:
        db_table = 'customer_memo'

