# coding=utf-8
import traceback
# import test_alchemy
# import test_spider
from src.proxy import proxy as pool
import time


# def tests():
#     test_alchemy.test_alchemy()
#     test_spider.test_spider()


def test_start():
    try:
        log = Logger(name='proxy.log')
        controller = pool.ProxyPool(log, False)
        # proxies = controller.spider.get_proxies(False)
        # controller.add_proxies(proxies)

        time.sleep(120)
        controller.export(r'D:\\')

        # proxy = controller.get_proxy()
        # controller.dispose()
        # controller.logger.dispose()
    except Exception:
        print(traceback.format_exc())


if __name__ == '__main__':
    # tests()
    test_start()
    # res = requests.head('http://www.baidu.com', proxies={'http': '61.135.217.7:80'})
    # res = requests.get('https://cn.bing.com/', verify=False)
    # soup = BeautifulSoup(res.text, "html.parser")
    # title = soup.title
    # str = title.string
    # if str == u'微软 Bing 搜索 - 国内版':
    #     print('haha')
    # print(res)
