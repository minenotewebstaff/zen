# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, date

# Create your models here.
class Customer(models.Model):
    SEX_CHOICES = (
        ('M', u'男性'),
        ('F', u'女性'),
    )
    sei  = models.CharField(u'姓', max_length=100)
    mei  = models.CharField(u'名', max_length=100)
    kanasei = models.CharField(u'かな姓', max_length=100)
    kanamei = models.CharField(u'かな名', max_length=100)
    zip  = models.CharField(u'郵便番号', max_length=7)
    pref = models.CharField(u'都道府県', max_length=20)
    add1 = models.CharField(u'住所1', max_length=256)
    add2 = models.CharField(u'住所2', max_length=256, blank=True)
    tel1  = models.CharField(u'TEL', max_length= 20)
    tel1_is_mobile = models.BooleanField(default= False)
    tel2 = models.CharField(u'TEL2', max_length = 20, blank=True)
    tel2_is_mobile = models.BooleanField(default= False)
    email1 = models.CharField(u'email', max_length=100)
    email1_is_mobile = models.BooleanField(default= False)
    email2 = models.CharField(u'email2', max_length=100, blank=True)
    email2_is_mobile = models.BooleanField(default= False)
    sex  = models.CharField(u'性別', max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(u'生年月日', null=True, blank=True)
    age  = models.IntegerField(u'年齢', null=True, blank=True)
    occupation = models.CharField(u'職業', max_length=100, blank=True)
    first_contact = models.DateField(u'初回接触', null=True, blank=True)
    first_buy = models.DateField(u'初回購入日', null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s: %s%s %s' % (self.sei, self.mei, self.pref, self.add1, self.tel)
    
    def name(self):
        return '%s %s' % (self.sei, self.mei)
    
    def kana(self):
        return '%s %s' % (self.kanasei, self.kanamei)
    

class CustomerMemo(models.Model):
    customer = models.ForeignKey(Customer)
    memo_date = models.DateTimeField(u'メモ追加日時', default=datetime.now())
    subject = models.CharField(u'メモタイトル', max_length=100)
    memo = models.TextField(u'追加顧客メモ')

    def __unicode__(self):
        return self.subject


class Size(models.Model):
    name = models.CharField(u'サイズ名', max_length=20)


class Item(models.Model):
    code = models.CharField(u'商品コード', max_length=20, unique=True)
    name = models.CharField(u'商品名', max_length=100)
    price = models.IntegerField(u'単価', default=0)
    memo = models.TextField(u'商品メモ', blank=True)
    
    def __unicode__(self):
        return '%s %s %d円' % (self.code, self.name, self.price)


class SalesSlip(models.Model):
    PAYMENT_CHOICES = (
        ('D',   u'代引き'),
        ('Y',   u'宅急便コレクト'),
        ('C',   u'クレジットカード'),
    )
    customer = models.ForeignKey(Customer)
    orders_date = models.DateTimeField(u'注文日時', default=datetime.now())
    shipping_date = models.DateField(u'出荷日', null=True, blank=True)
    payment = models.CharField(u'支払方法', max_length=1, choices=PAYMENT_CHOICES)
    recievers_zip  = models.CharField(u'届け先郵便番号', max_length=7)
    recievers_pref = models.CharField(u'届け先都道府県', max_length=20)
    recievers_add1 = models.CharField(u'届け先住所1', max_length=256)
    recievers_add2 = models.CharField(u'届け先住所2', max_length=256, blank=True)
    recievers_tel1 = models.CharField(u'届け先TEL', max_length= 20)
    delivery_time = models.DateField(u'お届け希望日', null=True, blank=True)
    is_present = models.BooleanField(u'プレゼント包装有り無し', default=False)
    opinion = models.TextField(u'ご意見・ご要望', blank=True)
    memo = models.TextField(u'備考', blank=True)
    
    def __unicode__(self):
        return u'%s 注文' % (self.orders_date.strftimr('%Y/%m%d %H:%M'))


class Sales_Detail(models.Model):
    salesslip = models.ForeignKey(SalesSlip)
    item = models.ForeignKey(Item)
    price = models.IntegerField(u'単価', default=0)
    size = models.ForeignKey(Size)
    quantity = models.IntegerField(u'数量', default=0)
    memo = models.TextField(u'備考', blank=True)
    
    def __unicode__(self):
        return '%s %s %d円 %d個 %d円' % (self.item.name, self.size.name, self.price, self.quantity, subtotal(self))
    
    def subtotal(self):
        return self.price * self.quantity




