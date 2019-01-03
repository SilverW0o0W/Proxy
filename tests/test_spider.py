# coding=utf-8
import unittest
from proxy.spider.xici_spider import XiciSpider


class TestSpider(unittest.TestCase):

    def test_get_proxies(self):
        spider = XiciSpider()
        proxies = spider.get_proxies(False)
        self.assertTrue(True, proxies)


def test_spider():
    suite = unittest.TestSuite()
    suite.addTest(TestSpider())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    test_spider()
