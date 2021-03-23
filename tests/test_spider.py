# coding=utf-8
import unittest
from proxy.spiders.kuai_spider import KuaiSpider


class TestSpider(unittest.TestCase):

    def test_get_proxies(self):
        spider = KuaiSpider()
        status, msg, proxies = spider.get_proxies(1)
        self.assertTrue(True, proxies)


def test_spider():
    suite = unittest.TestSuite()
    suite.addTest(TestSpider())
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    test_spider()
