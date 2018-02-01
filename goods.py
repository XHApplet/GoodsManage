#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    def __init__(self):
        self.GoodsInfo = {}

    def Load(self, dInfo):
        self.GoodsInfo = dInfo

    def Save(self):
        pass

    def GetGoodsName(self):
        return [ sName for sName in self.GoodsInfo ]



class CGoods(object):
    pass


def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
