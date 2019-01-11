import requests
import grequests


def request_response(url, proxies, timeout=5):
    status, response = False, None
    try:
        with requests.Session() as session:
            session.keep_alive = False
            response = session.get(url, proxies=proxies, timeout=timeout, allow_redirects=False, verify=False)
            status = response.status_code == 200 and response.url == response.request.url
    except requests.exceptions.RequestException:
        status = False
    except Exception:
        status = False
    finally:
        return status, response


def request_response(url, proxies_list, timeout=5):
    status, response = False, None
    try:
        status = response.status_code == 200 and response.url == response.request.url
    except requests.exceptions.RequestException:
        status = False
    except Exception:
        status = False
    finally:
        return status, response
