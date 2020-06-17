from django.conf import settings
from django.db import models
from django.utils import timezone


class Pcalc_info(models.Model):

    SEX = (('0', 'М'),('1','Ж' ))
    sex = models.CharField(max_length=10, choices=SEX, default='0')
    year_born = models.CharField(max_length=10)
    year_begin = models.CharField(max_length=10, default='2015') 
    ts01 = models.CharField(max_length=10, default='0')
    ts91 = models.CharField(max_length=10, default='0')
    szar5 = models.CharField(max_length=20, default='0')
    szar2 = models.CharField(max_length=20, default='0')
    ts14 = models.CharField(max_length=10, default='12')
    szar14 = models.CharField(max_length=20, default='0')
    szar15 = models.CharField(max_length=20 , default='0')
    sam = models.CharField(max_length=10, default='0')
    ssam = models.CharField(max_length=20, default='0')
    army = models.CharField(max_length=10, default='0')
    child = models.CharField(max_length=10, default='0')
    other = models.CharField(max_length=10, default='0')
    stn1 = models.CharField(max_length=10, default='0')
    stn2 = models.CharField(max_length=10, default='0')
    sts = models.CharField(max_length=10, default='0')
    stl1 = models.CharField(max_length=10, default='0')
    stl2 = models.CharField(max_length=10, default='0')
    pensia = models.CharField(max_length=40, default='0')

    
