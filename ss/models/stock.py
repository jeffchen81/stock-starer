# -*- coding: utf-8 -*-
# another: Jeff.Chen
from peewee import *


# config db
DATABASE = 'stock.db'

db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    """
    基类，连接指定db
        :param Model:
    """
    class Meta:
        database = db


class Stock(BaseModel):
    """
    股票记录表
        :param BaseModel:
    """
    stock_code = CharField()  # 股票代号: str(200)
    log_date = DateTimeField()  # 记录日期：date
    timestamp = DateTimeField()  # 记录时间：datetime
    yesterday_close_price = FloatField()  # 昨日收盘价：float
    today_open_price = FloatField()  # 今日开盘价：float
    current_price = FloatField()  # 当前价格：float
    buy_price = FloatField()  # 竞买价：float
    sell_price = FloatField()  # 竞卖价：float
    deal_num = IntegerField()  # 成交股票数量（股）：int
    deal_total = FloatField()  # 成交金额总数（元）：float


def create_tables():
    """
    建库
    """
    with db:
        db.create_tables([Stock])


if __name__ == '__main__':
    create_tables()