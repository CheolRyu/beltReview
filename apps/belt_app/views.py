# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'belt_app/index')

# Create your views here.
