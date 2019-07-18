#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""
from proxy import const


class PoolBase(object):
    """
    This is the class for crawling ip from proxy site
    """

    def __init__(self, spider, validator):
        self.spider = spider
        self.validator = validator

    def get_proxies(self, string=False):
        """
        Return proxies
        :param: string:
        :param: string:
        :return: proxies
        """
        return []
