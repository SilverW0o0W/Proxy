#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
This is for crawling proxy ip from ip website.
HTTP ONLY
"""

import traceback

from lxml import etree
from proxy import const
from proxy import requests
from proxy.spider.spider import SpiderBase
from proxy.proxy import Proxy


class KuaiSpider(SpiderBase):
    """
    HTTP ONLY
    """
    _user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    _header = {'User-Agent': _user_agent}
    ha_url_model = 'https://www.kuaidaili.com/free/inha/{}'
    limit_page = 5

    def __init__(self):
        self.running = False
        self.page = 1

    def get_proxies(self, protocols=None, proxies=None, **kwargs):
        """
        Get proxy ip
        """
        if self.running:
            return False, "", []
        self.running = True
        proxies = {} if proxies is None else proxies
        page = self.get_page()
        try:
            url = self.ha_url_model.format(page)
            status, response = requests.request("GET", url, verify=False, headers=self._header, proxies=proxies)
            if status and response.status_code != 200:
                return False, "", []
            return True, "", self.convert_proxies(response)
        except Exception:
            return False, traceback.format_exc(), []
        finally:
            self.running = False

    def get_page(self):
        page = self.page
        self.page += 1
        if self.page > self.limit_page:
            self.page = 1
        return page

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
