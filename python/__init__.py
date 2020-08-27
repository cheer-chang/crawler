# coding=utf-8

import sys
from eastmoney import Eastmoney
from my_logger import log
from my_schedule import run_schedule
from my_thread_pool_executor import MyThreadPoolExecutor

reload(sys)  # 设置系统默认编码
sys.setdefaultencoding('utf-8')  # 添加该方法声明编码

if __name__ == '__main__':
    future = MyThreadPoolExecutor.add(run_schedule)  # 启动定时任务
    log.info('start %s', not future.done())
    MyThreadPoolExecutor.add(Eastmoney().get)  # 爬取东方财富
    log.info('end...')
