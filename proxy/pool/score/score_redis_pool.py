#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This is for crawling proxy ip from ip website.
"""
import time
import redis

from proxy import const
from proxy.pool.score.score_pool import ScoreProxy, ScorePool


class ScoreRedisPool(ScorePool):
    """
    This is the class for crawling ip from proxy site
    """

    def __init__(self, spider, validator, config):
        super().__init__(spider, validator)
        self.config = config
        self.redis = redis.StrictRedis(**self.config["PROXY_REDIS"])

    def start(self):
        pass
