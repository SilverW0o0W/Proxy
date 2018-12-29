# coding=utf-8
"""
This is for controlling proxy ip
"""


class Proxy(object):

    def __init__(self, ip, port, protocol, score=0, created_time=None, verified_time=None):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.score = score
        self.created_time = created_time
        self.verified_time = verified_time

    def __str__(self):
        return self.ip + ':' + self.port
