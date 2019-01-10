# coding=utf-8

from proxy import const
from proxy.proxy import Proxy


class ScoreProxy(Proxy):

    def __init__(self, ip, port, protocol, score, created_time, updated_time):
        super().__init__(ip, port, protocol)
        self.score = score
        self.created_time = created_time
        self.updated_time = updated_time
