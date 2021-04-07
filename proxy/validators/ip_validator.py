#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

from proxy.const import const
from proxy.validator import Validator


class IPValidator(Validator):
    url_mapping = {
        const.HTTP: "http://api.ipify.org/",
        const.HTTPS: "https://api.ipify.org/",
    }

    def __init__(self, local_ip):
        self.local_ip = local_ip

    def check_proxy(self, proxy):
        """
        Check proxy available. Timeout: 15s. Retry: 3 times.
        """
        protocol = proxy.protocol
        url = self.url_mapping[protocol]
        proxies = proxy.to_proxies()
        status, response = self.request_response(url, proxies)
        return self.check_response(proxy, response) if status else status

    def check_response(self, proxy, response):
        """
        Check response content
        :param proxy:
        :param response:
        :return: is valid proxy
        """
        ip_text = response.text
        pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        if not pattern.match(ip_text):
            return False

        return self.local_ip != response.text
