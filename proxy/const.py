#!/usr/bin/env python
# -*- encoding: utf-8 -*-

HTTP = 1
HTTPS = 2
PROTOCOLS = [HTTP, HTTPS, ]
PROTOCOLS_MAP = {
    HTTP: 'HTTP',
    HTTPS: 'HTTPS',
}

SUCCESS = 1
WARN = 2
ERROR = 3
FATAL = 4
