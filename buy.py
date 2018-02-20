#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import mydefines

from mytool import pubdefines

TABLE_NAME="tbl_buy"
TABLE_CREAT_SQL="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Type text not null,
    Goods text not null,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME


class CBuyManager(object):

    ColInfo = [
        ("Time", "integer"),
        ("Type", "text"),
        ("Goods", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
    ]

    def __init__(self):
        self.BuyInfo = {}

    def InputGoods(self, tData):
        """进货保存数据库"""
        sql = mydefines.get_insert_sql(TABLE_NAME, tData, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def QueryAllInfo(self):
        """查询所有的进货信息"""
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy query:%s %s" % (ID, tData))
            self.BuyInfo[ID] = tData


    def GetBuyInfo(self, iBegin, iEnd):
        dBuyInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy info:%s %s" % (ID, tData))
            dBuyInfo[ID] = tData
        return dBuyInfo


    def GetBuyInfoRecord(self, iBegin, iEnd, sGoods):
        dBuyInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        if sGoods:
            sql = sql + " and Goods like '%%%s%%'" % sGoods
        sql += " ORDER BY Time"
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy record:%s %s" % (ID, tData))
            dBuyInfo[ID] = tData
        return dBuyInfo


def InitBuy():
    oBugMgr = CBuyManager()
    pubdefines.set_manager("buymgr", oBugMgr)
