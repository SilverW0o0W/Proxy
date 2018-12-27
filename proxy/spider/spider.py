#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""


class Spider(object):
    """
    This is the class for crawling ip from proxy site
    """

    def get_proxies(self, url, params=None, https=False):
        """
        Return proxies
        :param url: url
        :param params: params
        :param https: https
        :return: status, msg, proxies_list
        """
        return False, "", []
