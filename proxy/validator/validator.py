#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

"""
Check proxy available
"""


class ValidatorBase(object):
    timeout = 15

    @staticmethod
    def check_proxy(proxy):
        return 0

    @classmethod
    def request_response(cls, url, proxies):
        status, response = False, None
        try:
            with requests.Session() as session:
                session.keep_alive = False
                response = session.get(url, proxies=proxies, timeout=cls.timeout, allow_redirects=False, verify=False)
                status = response.status_code == 200 and response.url == response.request.url
        except requests.exceptions.RequestException:
            status = False
        except Exception:
            status = False
        finally:
            return status, response
