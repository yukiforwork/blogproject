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
    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name = 'blog_detail'
        ),
    path(
        'science-list/',
        views.ScienceView.as_view(),
        name = 'science_list'
        ),
    path(
        'dailylife-list/',
        views.DailylifeView.as_view(),
        name = 'dailylife_list'
        ),
    path(
        'music-list/',
        views.MusicView.as_view(),
        name = 'music_list'
        ),
]