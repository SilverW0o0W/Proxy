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
            proxies = {'HTTPS': str(proxy)}
            url = ""
        else:
            proxies = {'HTTP': str(proxy)}
            url = ""

        with requests.Session() as session:
            try:
                session.keep_alive = False
                response = session.get(url, proxies=proxies, timeout=15, verify=False)
                proxy.available = cls.check_response(response, url)
            except requests.exceptions.RequestException:
                proxy.available = False
            except Exception as ex:
                print(ex)
        return proxy.available

    @staticmethod
    def check_response(response, url):
        """
        Check response content
        :param response:
        :param url:
        :return: is valid proxy
        """
        # Check 1st: response status == 200 and url is right
        if response.status_code != 200 or response.url != url:
            return False
        # Check 2nd: response content is real
        return 0
