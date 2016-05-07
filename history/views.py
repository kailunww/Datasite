# -*- coding: utf-8 -*-
#
from django.shortcuts import render

from django.http import HttpResponse
from models import Counter


def here(request):
    count = Counter().count
    return HttpResponse(str(count))
