#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from proxy import const
from proxy.validator.validator import Validator


class IPValidator(Validator):
    url_mapping = {
        const.HTTP: "https://api.ipify.org/",
        const.HTTPS: "https://api.ipify.org/",
    }
    http_url = "http://api.ipify.org/"

    def __init__(self):
        pass

    @classmethod
    def check_proxy(cls, proxy, first=False, ):
        """
        Check proxy available. Timeout: 15s. Retry: 3 times.
        """
        protocol = proxy.protocol
        url = cls.url_mapping[protocol]
        proxies = proxy.to_proxies()
        status, response = cls.request_response(url, proxies)
        return cls.check_proxy(proxy, response) if status else status

    @staticmethod
    def check_response(proxy, response):
        """
        Check response content
        :param proxy:
        :param response:
        :return: is valid proxy
        """
        return proxy.ip == response.text
