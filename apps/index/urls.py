# -*- coding: utf-8 -*- #
"""
    Created on 04.04.15 by fashust
    index urls patterns
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url, patterns

from .views import IndexViewHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


urlpatterns = patterns(
    'apps.index',
    url(r'^$', IndexViewHandler.as_view(), name='index'),
)