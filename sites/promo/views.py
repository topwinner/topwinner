#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):
    ctx = {'current_url':'promo_index'}
    return render(request, 'promo/promo.html', ctx)

def limitedtimediscount(request):
    ctx = {'current_url':'promo_index','promo_type':'limitedtimediscount','tools_name':'限时打折'}
    return render(request, 'promo/limitedtimediscount.html', ctx)

def fullrewards(request):
    ctx = {'current_url':'promo_index','promo_type':'fullrewards','tools_name':'满就送'}
    return render(request, 'promo/fullrewards.html', ctx)

def buymore(request):
    ctx = {'current_url':'promo_index','promo_type':'buymore','tools_name':'多买优惠'}
    return render(request, 'promo/buymore.html', ctx)

def freeshipping(request):
    ctx = {'current_url':'promo_index','promo_type':'freeshipping','tools_name':'包邮'}
    return render(request, 'promo/freeshipping.html', ctx)