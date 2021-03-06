# coding=utf-8

from proxy.const import const


class Proxy(object):

    def __init__(self, ip=None, port=None, protocol=None):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def __str__(self):
        return "{}:{}".format(self.ip, self.port)

    def to_proxies(self):
        protocol = "http" if self.protocol == const.HTTP else "https"
        return {
            protocol: "{}://{}".format(protocol, self)
        }
