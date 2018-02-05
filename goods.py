#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import mydefines
from mytool import pubdefines

TABLE_NAME="tbl_goods"
TABLE_CREAT_SQL="""
create table %s
(
    Goods text PRIMARY KEY not null,
    BuyPrice integer not null,
    SellPrice integer not null,
    Num integer not null
)
""" % TABLE_NAME


class CGoodsManager(object):

    ColInfo = [
        ("Goods", "text"),
        ("BuyPrice", "integer"),
        ("SellPrice", "integer"),
        ("Num", "integer"),
    ]
    KeyNum = 1

    def __init__(self):
        self.GoodsInfo = {}
        self.Load()

    def GetGoodsInfo(self):
        return self.GoodsInfo

    def GetGoodsBuyPrice(self, sGoods):
        tInfo = self.GoodsInfo.get(sGoods, None)
        assert tInfo is not None
        return tInfo[0]

    def InputGoods(self, sGoods, fBuyPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.NewGoodsInfo(sGoods)
        tInfo = self.GoodsInfo[sGoods]
        tInfo[0] = fBuyPrice
        tInfo[2] += iNum
        self.Update(sGoods, tInfo)

    def OutputGoods(self, sGoods, fSellPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.NewGoodsInfo(sGoods)
        tInfo = self.GoodsInfo[sGoods]
        tInfo[1] = fSellPrice
        tInfo[2] -= iNum
        self.Update(sGoods, tInfo)

    def NewGoodsInfo(self, sGoods):
        self.GoodsInfo[sGoods] = [0, 0, 0]
        sql = mydefines.get_insert_sql(TABLE_NAME, [sGoods, 0, 0, 0], self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def Update(self, sGoods, tInfo):
        lstSet = []
        for iIndex, value in enumerate(tInfo):
            sColName, sType = self.ColInfo[iIndex + self.KeyNum]
            value = mydefines.get_insert_value(value, sType)
            lstSet.append("%s=%s" % (sColName, value))
        sSet = ",".join(lstSet)
        sql = "update %s set %s where Goods='%s'" % (TABLE_NAME, sSet, sGoods)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def Load(self):
        logging.info("%s load" % TABLE_NAME)
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for sGoods, *tInfo in result:
            self.GoodsInfo[sGoods] = tInfo
            logging.debug("load: %s %s" % (sGoods, tInfo))
        logging.info("    load finish %s" % len(result))



def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
