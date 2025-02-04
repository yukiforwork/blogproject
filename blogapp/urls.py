#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:16:02 2025

@author: yuki
"""

from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]