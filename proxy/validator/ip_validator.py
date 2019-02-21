#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from proxy import const
from proxy.validator.validator import ValidatorBase


class IPValidator(ValidatorBase):
    url_mapping = {
        const.HTTP: "https://api.ipify.org/",
        const.HTTPS: "https://api.ipify.org/",
    }
    http_url = "http://api.ipify.org/"

    def __init__(self):
        pass

    @classmethod
    def check_proxy(cls, proxy):
        """
        Check proxy available. Timeout: 15s. Retry: 3 times.
        """
        protocol = proxy.protocol
        url = cls.url_mapping[protocol]
        proxies = proxy.to_proxies()
        try:
            response = cls.request_response(url, proxies)
            if response:
                if response.status_code == 200:
                    status = const.SUCCESS if cls.check_response(proxy, response) else const.FATAL
                else:
                    status = const.WARN
            else:
                status = const.ERROR
        except Exception:
            status = const.FATAL
        return status

    @staticmethod
    def check_response(proxy, response):
        """
        Check response content
        :param proxy:
        :param response:
        :return: is valid proxy
        """
        return response.url == response.request.url and proxy.ip == response.text
