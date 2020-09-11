# coding=utf-8

import sys
import request
import database
from service.eastmoney import Eastmoney
from util.my_logger import log
from util.my_schedule import run_schedule
from util.my_thread_pool_executor import MyThreadPoolExecutor
from entity.user_test import UserTest

reload(sys)  # 设置系统默认编码
sys.setdefaultencoding('utf-8')  # 添加该方法声明编码

if __name__ == '__main__':
    database.DBSession = database.get_session("root", "root", "localhost", "3306", "test")  # 连接数据库
    future = MyThreadPoolExecutor.add(run_schedule)  # 启动定时任务
    log.info('start %s', not future.done())
    MyThreadPoolExecutor.add(Eastmoney().get)  # 爬取东方财富
    MyThreadPoolExecutor.add(request.test_req)  # 请求大盘板块信息

    ut = UserTest()
    ut.get()
    log.info('end...')
