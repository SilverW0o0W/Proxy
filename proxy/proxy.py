# coding=utf-8

from proxy import const


class Proxy(object):

    def __init__(self, ip, port, protocol, score=0, created_time=None, verified_time=None):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.score = score
        self.created_time = created_time
        self.verified_time = verified_time

    def __str__(self):
        return "{}:{}".format(self.ip, self.port)

    def to_proxies(self):
        return {
            "http" if self.protocol == const.HTTP else "https": str(self)
        }
