#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

http_url = ""
https_url = ""


def verify_proxy():
    pass


def check_proxy(proxy, https=False):
    """
    Check proxy available. Timeout: 15s. Retry: 3 times.
    """
    if https:
        url = https_url
        transfer_method = "https"
    else:
        url = http_url
        transfer_method = "http"

    proxies = {transfer_method: str(proxy)}
    requests.adapters.DEFAULT_RETRIES = 3
    with requests.Session() as session:
        try:
            session.keep_alive = False
            if https:
                response = session.get(url, proxies=proxies, timeout=30, verify=False)
            else:
                response = session.get(url, proxies=proxies, timeout=15)
            proxy.available = check_response(response, url)
        except requests.exceptions.RequestException:
            proxy.available = False
        except Exception as ex:
            print(ex)
    return proxy.available


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