#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from proxy.constants import Constants

const = Constants()

const.HTTP = 1
const.HTTPS = 2
const.PROTOCOLS = [const.HTTP, const.HTTPS, ]
const.PROTOCOLS_MAP = {
    const.HTTP: 'HTTP',
    const.HTTPS: 'HTTPS',
}
