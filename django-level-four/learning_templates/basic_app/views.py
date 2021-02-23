# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello world', 'number':400}
    return render(request, 'index.html',context_dict)

def other(request):
    return render(request, 'other.html')


def relative(request):
    return render(request, 'relative_url_templates.html')