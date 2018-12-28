#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
This is for crawling proxy ip from ip website.
"""

import traceback

import requests
from bs4 import BeautifulSoup
from proxy import const
from proxy.spider.spider import Spider
from proxy.proxy import Proxy


class XiciSpider(Spider):
    _user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    _header = {'User-Agent': _user_agent}
    url_model = {
        const.HTTP: 'http://www.xicidaili.com/nn/',
        const.HTTPS: 'http://www.xicidaili.com/nn/',
    }
    _http_url = 'http://www.xicidaili.com/wt/'
    _https_url = 'http://www.xicidaili.com/wn/'
    _anon_url = 'http://www.xicidaili.com/nn/'

    def get_proxies(self, url, protocols=None, **kwargs):
        """
        Get proxy ip
        """
        protocols = [const.HTTP, ] if protocols is None else protocols
        try:
            response = requests.get(url, headers=self._header)
            if response.status_code != 200:
                return False, "", []
            return True, "", self.convert_proxies(response, protocols)
        except Exception:
            return False, traceback.format_exc(), []

    @classmethod
    def convert_proxies(cls, response, protocols):
        soup = BeautifulSoup(response.text, "html.parser")
        ip_table = soup.find(id='ip_list')
        ips = ip_table.findAll('tr')
        proxies = list(filter(None, [cls.convert_proxy(ip) for ip in ips[1:]]))
        return [proxy for proxy in proxies if proxy.https == https] if https else proxies

    @staticmethod
    def convert_proxy(ip):
        tds = ip.findAll("td")
        if not tds[4].contents[0] == '高匿':
            return
        is_https = tds[5].contents[0] == 'HTTPS'
        return Proxy(tds[1].contents[0], tds[2].contents[0], is_https)
