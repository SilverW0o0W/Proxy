#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from proxy import const
from proxy.validator.validator import Validator


class IPValidator(Validator):

    def __init__(self):
        pass

    @staticmethod
    def check_proxy(proxy):
        """
        Check proxy available. Timeout: 15s. Retry: 3 times.
        """
        protocol = proxy.protocol
        if protocol == const.HTTPS:
            proxies = {'HTTPS': str(proxy)}
        else:
            proxies = {'HTTP': str(proxy)}

        with requests.Session() as session:
            try:
                session.keep_alive = False
                if https:
                    response = session.get(url, proxies=proxies, timeout=15, verify=False)
                else:
                    response = session.get(url, proxies=proxies, timeout=15)
                proxy.available = check_response(response, url)
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
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title
        check_title = self._https_title if self.https else self._http_title
        return title is not None and title.string == check_title
