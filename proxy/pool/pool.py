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

    def __init__(self, spider, validator, protocol=const.HTTP):
        self.spider = spider
        self.validator = validator
        self.protocol = protocol

    def get_proxies(self, protocol=const.HTTP, string=False):
        """
        Return proxies
        :param: string:
        :param: string:
        :return: proxies
        """
        return []
