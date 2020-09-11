# coding=utf8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from util.my_logger import log

DBSession = None  # 创建一个操作数据库的会话
BaseEntity = declarative_base()  # 实体对象的基类


def get_session(user, password, host, port, db):
    try:
        if DBSession is None:
            url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, db)
            log.info(url)
            log.info("开始连接数据库...")
            # engine = create_engine(url, echo=True)
            engine = create_engine(url)
            log.info("数据库连接成功...")
            session = sessionmaker(bind=engine)
            log.info("会话已创建")
            return session()
        else:
            return DBSession
    except Exception as e:
        log.error("数据库连接失败...")
        log.error(e.args)
