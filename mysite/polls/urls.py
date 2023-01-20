# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:17:44 2023

@author: eevae
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]