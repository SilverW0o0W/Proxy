#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""
from proxy import const


class SpiderBase(object):
    """
    This is the class for crawling ip from proxy site
    """

    def get_proxies(self, url, protocols=None, **kwargs):
        """
        Return proxies
        :param url: url
        :param protocols: protocols
        :return: status, msg, proxies_list
        """
        return False, "", []
