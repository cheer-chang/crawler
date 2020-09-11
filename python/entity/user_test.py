# coding=utf8
from sqlalchemy import Column, String, Integer, BigInteger

import database
from util.my_logger import log


class UserTest(database.BaseEntity):
    __tablename__ = "user_test"
    id = Column(BigInteger, primary_key=True)
    age = Column(Integer)
    name = Column(String(255))
    creator_id = Column(Integer())

    def __init__(self):
        pass

    def get(self):
        ut = database.DBSession.query(UserTest).filter(UserTest.id == 41).one()
        log.info(ut.id)
        log.info(ut.name)
