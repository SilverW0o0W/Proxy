# coding=utf-8
import unittest
from proxy.spider.xici_spider import XiciSpider


class TestSpider(unittest.TestCase):

    def __init__(self):
        unittest.TestCase.__init__(self)
        self.spider = XiciSpider()

    def test_get_proxies(self):
        count = self.spider.get_proxies(False)
        self.assertGreater(0, count)


def test_spider():
    suite = unittest.TestSuite()
    suite.addTest(TestSpider())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    test_spider()
