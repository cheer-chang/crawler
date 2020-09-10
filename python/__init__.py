# coding=utf-8

import sys
import request
from service.eastmoney import Eastmoney
from util.my_logger import log
from util.my_schedule import run_schedule
from util.my_thread_pool_executor import MyThreadPoolExecutor

reload(sys)  # 设置系统默认编码
sys.setdefaultencoding('utf-8')  # 添加该方法声明编码

if __name__ == '__main__':
    future = MyThreadPoolExecutor.add(run_schedule)  # 启动定时任务
    log.info('start %s', not future.done())
    MyThreadPoolExecutor.add(Eastmoney().get)  # 爬取东方财富
    MyThreadPoolExecutor.add(request.test_req)  # 请求大盘板块信息
    log.info('end...')
