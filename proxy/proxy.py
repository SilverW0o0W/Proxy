# coding=utf-8
"""
This is for controlling proxy ip
"""


class Proxy(object):

    def __init__(self, ip, port, protocol, score=20, created=None, verified=None):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.score = score
        self.created_time = created
        self.verified_time = verified

    def __str__(self):
        return self.ip + ':' + self.port
