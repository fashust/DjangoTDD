# -*- coding: utf-8 -*- #
"""
    Created on 04.04.15 by fashust
    index page app tests
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class IndexPageTestCases(TestCase):
    """
        index page test cases
    """
    def test_status_code(self):
        """
            test page open status code
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)