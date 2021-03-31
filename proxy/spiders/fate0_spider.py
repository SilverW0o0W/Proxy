#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import io
import json

import requests
from proxy.const import const
from proxy.spider import Spider
from proxy.proxy import Proxy


class Fate0Spider(Spider):
    _user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    _header = {'User-Agent': _user_agent}
    proxy_url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"

    def get_proxies(self, protocols=None, proxies=None, **kwargs):
        """
        Get proxy ip
        """
        proxies = {} if proxies is None else proxies
        try:
            response = requests.get(self.proxy_url, headers=self._header, proxies=proxies, timeout=10)
            if response.status_code != 200:
                return False, "", []
            return True, "", self.convert_proxies(response)
        except BaseException as ex:
            return False, str(ex), []

    @classmethod
    def convert_proxies(cls, response):
        proxies = []
        str_content = str(response.content, encoding="utf-8")
        with io.StringIO(str_content) as lines:
            for line in lines:
                json_item = json.loads(line)
                status, proxy = cls.convert_proxy(json_item)
                if not status:
                    continue
                proxies.append(proxy)

        return proxies

    @staticmethod
    def convert_proxy(values):
        try:
            _type = values.get("type", "")
            if _type == "http":
                protocol = const.HTTP
            elif _type == "https":
                protocol = const.HTTPS
            else:
                return False, None

            proxy = Proxy(
                values["host"],
                int(values["port"]),
                protocol
            )
        except BaseException:
            return False, None
        else:
            return True, proxy
