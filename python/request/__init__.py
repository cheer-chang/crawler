#!coding=utf-8
from util.my_logger import log
from request.request_util import RequestUtil


def test_req():
    log.info("开始请求...")
    req = RequestUtil()
    i = 0
    while i < 10:
        # https://x-quote.cls.cn/quote/index/tline?app=CailianpressWeb&date=20200821&os=web&sv=7.2.2&sign=19451680ce43b6be73f28481e91cfc32
        res = req.get(
            'https://x-quote.cls.cn/quote/index/tline?app=CailianpressWeb&date=20200821&os=web&sv=7.2.2&sign=19451680ce43b6be73f28481e91cfc32')
        res2 = req.get(
            'https://www.cls.cn/v3/transaction/anchor?app=CailianpressWeb&cdate=2020-08-21&os=web&sv=7.2.2&sign=c1a1f220a04f4aa92d04bc57bc4a9836')

        log.info(res.status_code)
        log.info(res.text)
        log.info(res2.status_code)
        log.info(res2.text)
        i = i + 1
    log.info("结束请求...")
    log.info("")
