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

    def __init__(self):
        self.GoodsInfo = {}
        self.Load()

    def InputGoods(self, sGoods, fBuyPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.GoodsInfo[sGoods] = [0, 0, 0]
        tInfo = self.GoodsInfo[sGoods]
        tInfo[0] = fBuyPrice
        tInfo[2] += iNum
        # TODO update
        self.Save((sGoods, *tInfo))

    def OutputGoods(self, sGoods, fSellPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.GoodsInfo[sGoods] = [0, 0, 0]
        tInfo = self.GoodsInfo[sGoods]
        tInfo[1] = fSellPrice
        tInfo[2] -= iNum
        self.Save((sGoods, *tInfo))

    def Save(self, tInfo):
        sql = mydefines.get_insert_sql(TABLE_NAME, tInfo, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def Load(self):
        logging.info("%s load" % TABLE_NAME)
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for sGoods, *tInfo in result:
            self.GoodsInfo[sGoods] = tInfo
            print(tInfo, type(tInfo))
            logging.debug("load: %s %s" % (sGoods, tInfo))
        logging.info("    load finish %s" % len(result))


class CGoods(object):
    pass


def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
