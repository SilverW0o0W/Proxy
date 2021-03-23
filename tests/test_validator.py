# coding=utf-8
import unittest
from proxy import const
from proxy.proxy import Proxy
from proxy.validators import IPValidator


class TestValidator(unittest.TestCase):

    def test_get_proxies(self):
        validator = IPValidator()
        test_proxy = Proxy('127.0.0.1', 8080, const.HTTP)
        status = validator.check_proxy(test_proxy)
        self.assertTrue(True, status)


def test_validator():
    suite = unittest.TestSuite()
    suite.addTest(TestValidator())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    test_validator()
