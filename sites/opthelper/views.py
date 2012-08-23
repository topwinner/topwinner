#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url,'opt_tools':'','tools_name':'店铺工具'}
    return render(request, 'opthelper/opthelper.html', ctx)

def autoshelves(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'autoshelves','tools_name':'自动上架'}
    return render(request, 'opthelper/autoshelves.html', ctx)

def autoshowcase(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'autoshowcase','tools_name':'自动橱窗'}
    return render(request, 'opthelper/autoshowcase.html', ctx)

def bulkediting(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'bulkediting','tools_name':'批量修改'}
    return render(request, 'opthelper/bulkediting.html', ctx)

def salespackage(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'salespackage','tools_name':'套餐搭配'}
    return render(request, 'opthelper/salespackage.html', ctx)

def salesrecommend(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'salesrecommend','tools_name':'宝贝推荐'}
    return render(request, 'opthelper/salesrecommend.html', ctx)

def groupbuytemplates(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'groupbuytemplates','tools_name':'团购模板'}
    return render(request, 'opthelper/groupbuytemplates.html', ctx)

def praiserecommended(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'praiserecommended','tools_name':'限时优惠'}
    return render(request, 'opthelper/praiserecommended.html', ctx)

def watermarks(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'watermarks','tools_name':'水印标签'}
    return render(request, 'opthelper/watermarks.html', ctx)
