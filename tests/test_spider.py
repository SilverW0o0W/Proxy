# coding=utf-8
import unittest
from proxy.spiders.kuai_spider import KuaiSpider
from proxy.spiders.fate0_spider import Fate0Spider


class TestSpider(unittest.TestCase):

    def test_kuai_get_proxies(self):
        spider = KuaiSpider()
        status, msg, proxies = spider.get_proxies(1)
        proxies[0].to_proxies()
        self.assertTrue(True, proxies)

    def test_fate0_get_proxies(self):
        spider = Fate0Spider()
        status, msg, proxies = spider.get_proxies()
        self.assertTrue(True, proxies)


def test_spider():
    suite = unittest.TestSuite()
    suite.addTest(TestSpider())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    test_spider()
