#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""
from proxy import const
from proxy.pool.pool import PoolBase


class ScorePool(PoolBase):
    """
    This is the class for crawling ip from proxy site
    """

    def get_proxies(self, protocol=const.HTTP, string=False):
        """
        Return proxies
        :param: string:
        :param: string:
        :return: proxies
        """
        return []

    def check_proxies(self, proxies):
        pass
