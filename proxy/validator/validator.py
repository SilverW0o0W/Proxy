#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from proxy import requests

"""
Check proxy available
"""


class ValidatorBase(object):
    timeout = 15

    @staticmethod
    def check_proxy(proxy):
        return 0

    @classmethod
    def get(cls, url, proxies):
        return requests.request("GET", url, proxies, timeout=cls.timeout)
