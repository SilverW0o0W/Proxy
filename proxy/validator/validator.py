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
    def request_response(cls, url, proxies):
        return requests.request_response(url, proxies, timeout=cls.timeout)
