# -*- coding: utf-8 -*- #
"""
    Created on 04.04.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.http import HttpResponse
from django.views.generic import View


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


__all__ = (
    'IndexViewHandler',
)


class IndexViewHandler(View):
    """
        simple index page
    """
    def get(self, request, *args, **kwargs):
        """
            get method handler
        """
        return HttpResponse()