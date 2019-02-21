#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import grequests
import requests


def request(method, url, _async=True, **kwargs):
    response = None
    try:
        if _async:
            req = grequests.request(method, url, **kwargs)
            # proxies=proxies, timeout=timeout, allow_redirects=False, verify=False
            rs = (req,)
            responses = grequests.map(rs)
            response = responses[0]
        else:
            with requests.Session() as session:
                response = session.request(method, url, **kwargs)
        # status = response.status_code == 200 and response.url == response.request.url
    except requests.exceptions.RequestException:
        response = None
    finally:
        return response
