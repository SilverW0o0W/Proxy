#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from proxy import const
from proxy.validator.validator import Validator


class IPValidator(Validator):

    def __init__(self):
        pass

    @classmethod
    def check_proxy(cls, proxy):
        """
        Check proxy available. Timeout: 15s. Retry: 3 times.
        """
        protocol = proxy.protocol
        if protocol == const.HTTPS:
            proxies = {'https': str(proxy)}
            url = "https://api.ipify.org/"
        else:
            proxies = {'http': str(proxy)}
            url = "http://api.ipify.org/"

        with requests.Session() as session:
            try:
                session.keep_alive = False
                response = session.get(url, proxies=proxies, timeout=15, allow_redirects=False, verify=False)
                available = cls.check_response(proxy, response)
            except requests.exceptions.RequestException:
                available = False
            except Exception as ex:
                print(ex)
        return available

    @staticmethod
    def check_response(proxy, response):
        """
        Check response content
        :param response:
        :return: is valid proxy
        """
        # Check 1st: response status == 200 and url is right
        if response.status_code != 200 or response.url != response.request.url:
            return False
        # Check 2nd: response content is real
        return proxy.ip == response.text
