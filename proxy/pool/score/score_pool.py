#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""
import time

from proxy import const
from proxy.proxy import Proxy
from proxy.pool.pool import PoolBase


class ScoreProxy(Proxy):

    def __init__(self, ip, port, protocol, score, created_time, updated_time):
        super().__init__(ip, port, protocol)
        self.score = score
        self.created_time = created_time
        self.updated_time = updated_time


class ScorePool(PoolBase):
    """
    This is the class for crawling ip from proxy site
    """

    STATUS_SCORE = {
        const.SUCCESS: 2,
        const.WARN: -2,
        const.ERROR: -5,
        const.FATAL: -20,
    }

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

    def crawl(self):
        status, msg, proxies = self.spider.get_proxies()
        now = time.time()
        checked_proxies = [
            self.build_score_proxy(proxy, 20, now, now)
            for proxy in proxies
            if self.validator.check_proxy(proxy) == const.SUCCESS
        ]

    @staticmethod
    def build_score_proxy(proxy, score, created_time, updated_time):
        return ScoreProxy(
            proxy.ip, proxy.port, proxy.protocol,
            score, created_time, updated_time
        )
