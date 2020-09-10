# -*-coding:utf8-*-
import json
import re
import bs4
from request.request_util import RequestUtil
from util.my_logger import log


class Eastmoney:
    def __init__(self):
        self.results = {}

    def get(self):
        # 东方财富
        url = 'http://stock.eastmoney.com/a/chyyj.html'
        # url = 'http://finance.eastmoney.com/a/ccjdd.html'
        # url = 'http://finance.eastmoney.com/a/202008121590598091.html'

        response = RequestUtil.get(url)

        code = response.status_code
        result = response.text
        log.info(code)
        if code != 200:
            return None

        # log.info result

        # 解析html
        soup = bs4.BeautifulSoup(result, 'html.parser')
        # 东方财富的查找
        pls = soup.find_all('a', href=re.compile(r'finance.eastmoney.com/a/'))
        self.parse_sub_page(pls)
        log.info('解析完成，开始打印数据...')
        for k, v in self.results.items():
            log.info(k)
            log.info(json.dumps(self.results.get(k), encoding='utf8', ensure_ascii=False))

    def parse_sub_page(self, pls):
        for p in pls:
            url = p['href']
            # 检查当前url是否已经解析过了
            # if self.results.has_key(url):
            if url in self.results:
                log.info(url + "\tparse repetition")
                continue
            else:
                log.info(url)

            response = RequestUtil.get(url)

            html = response.text
            # log.info(result2)
            # 解析html
            soup = bs4.BeautifulSoup(html, 'html.parser')
            # 去除不需要的标签
            [s.extract() for s in soup(['img', 'iframe', 'video'])]
            # 去除标签中不需要的属性
            # del soup.a["class"]
            # del soup.a["href"]
            # divs = soup.find_all().findall('div', __class=re.compile('newsContent')))
            h1 = soup.find('div', class_='newsContent').find('h1')
            time = soup.find('div', class_='newsContent').find('div', class_='time')
            source = soup.find('div', class_='newsContent').find('div', class_='source data-source')
            content_body = soup.find('div', class_='newsContent').find('div', id=re.compile('ContentBody'))
            # log.info("标题： %s" % h1)
            # log.info("时间：%s" % time)
            # log.info("来源：%s" % source)
            # log.info(h1)
            # log.info(time)
            # log.info(source)
            # log.info(content_body)

            result = {'title': h1.get_text(), 'time': time.get_text(),
                      'source': str(source.get_text()).replace("来源：", ""),
                      'content': str(content_body)}
            self.results.setdefault(url, result)
