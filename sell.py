#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
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
    Remark text,
    Profile real not null
)
""" % TABLE_NAME


class CSellManager(object):
    
    ColInfo = [
        ("Time", "integer"),
        ("Goods", "text"),
        ("Seller", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
        ("Profile", "real"),    #本次卖货的利润，便于统计总利润
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


    def GetSellInfo(self, iBegin, iEnd):
        dSellInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell info:%s %s" % (ID, tData))
            dSellInfo[ID] = tData
        return dSellInfo


    def GetSellInfoRecord(self, iBegin, iEnd, sGoods, sBuyer):
        dSellInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        if sGoods:
            sql = sql + " and Goods like '%%%s%%'" % sGoods
        if sBuyer:
            sql = sql + " and Seller like '%%%s%%'" % sBuyer
        sql += " ORDER BY Time"
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell record:%s %s" % (ID, tData))
            dSellInfo[ID] = tData
        return dSellInfo



def InitSell():
    oSellMgr = CSellManager()
    pubdefines.set_manager("sellmgr", oSellMgr)
