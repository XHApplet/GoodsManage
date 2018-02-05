#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mydefines

from mytool import pubdefines

TABLE_NAME="tbl_sell"
TABLE_CREAT_SQL="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Goods text not null,
    Seller text,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME


class CSellManager(object):
    
    ColInfo = [
        ("Time", "datetime"),
        ("Goods", "text"),
        ("Seller", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
    ]

    def __init__(self):
        self.SellInfo = {}

    def OutputGoods(self, tData):
        """出货保存数据库"""
        sql = mydefines.get_insert_sql(TABLE_NAME, tData, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def QueryAllInfo(self):
        """查询所有的进货信息"""
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell query:%s %s" % (ID, tData))
            self.SellInfo[ID] = tData


def InitSell():
    oSellMgr = CSellManager()
    pubdefines.set_manager("sellmgr", oSellMgr)
