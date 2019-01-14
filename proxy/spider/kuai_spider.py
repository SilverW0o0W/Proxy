#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
This is for crawling proxy ip from ip website.
"""

import traceback
import requests

from lxml import etree
from proxy import const
# from proxy import requests
from proxy.spider.spider import SpiderBase
from proxy.proxy import Proxy


class KuaiSpider(SpiderBase):
    _user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    _header = {'User-Agent': _user_agent}
    ha_url_model = 'https://www.kuaidaili.com/free/inha/{}'

    def get_proxies(self, page, protocols=None, proxies=None, **kwargs):
        """
        Get proxy ip
        """
        proxies = {} if proxies is None else proxies
        try:
            url = self.ha_url_model.format(page)
            response = requests.get(url, headers=self._header, proxies=proxies)
            if response.status_code != 200:
                return False, "", []
            return True, "", self.convert_proxies(response)
        except Exception:
            return False, traceback.format_exc(), []

    @classmethod
    def convert_proxies(cls, response):
        proxies = []
        selector = etree.HTML(response.text)
        ip_table = selector.xpath("//*[@id='list']/table/tbody/tr")
        for ip in ip_table:
            values = ip.xpath("td/text()")
            status, proxy = cls.convert_proxy(values)
            if status:
                proxies.append(proxy)

        return proxies

    @staticmethod
    def convert_proxy(values):
        try:
            return True, Proxy(
                str(values[0]),
                int(values[1]),
                const.HTTP
            )
        except Exception:
            return False, None
