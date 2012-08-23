#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'opttools/opthelper.html', ctx)

def autoshelves(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'autoshelves','tools_name':'自动上架'}
    return render(request, 'opttools/autoshelves.html', ctx)

def autoshowcase(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'autoshowcase','tools_name':'自动橱窗'}
    return render(request, 'opttools/autoshowcase.html', ctx)

def bulkediting(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'bulkediting','tools_name':'批量修改'}
    return render(request, 'opttools/bulkediting.html', ctx)

def salespackage(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'salespackage','tools_name':'套餐搭配'}
    return render(request, 'opttools/salespackage.html', ctx)

def salesrecommend(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'salesrecommend','tools_name':'宝贝推荐'}
    return render(request, 'opttools/salesrecommend.html', ctx)

def groupbutemplates(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'groupbutemplates','tools_name':'团购模板'}
    return render(request, 'opttools/groupbutemplates.html', ctx)

def praiserecommended(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'praiserecommended','tools_name':'限时优惠'}
    return render(request, 'opttools/praiserecommended.html', ctx)

def watermarks(request):
    ctx = {'current_url':'opthelper_index','opt_tools':'watermarks','tools_name':'水印标签'}
    return render(request, 'opttools/watermarks.html', ctx)
