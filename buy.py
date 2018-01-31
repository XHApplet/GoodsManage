#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pubdef

TABLE_NAME="tbl_buy"
TABLE_GOODS="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime null,
    Goods text null,
    Price real null,
    Num integer null,
    Remark text
)
""" % TABLE_NAME

class CBuyManager(object):
    def __init__(self):
        self.BuyInfo = {}

    def InputGoods(self, data, sGoods, fPrice, iNum, sRemark):
        sql = "insert into %s(Time, Goods, Price, Num, Remark) values('%s', '%s', %s, %s, '%s')" % (TABLE_NAME,
            data, sGoods, fPrice, iNum, sRemark)
        pubdef.CallManagerFunc("dbmgr", "Excute", sql)

    def Query(self):
        pass

class CBuy(object):
    ColType = {
        "Time"      :"time",
        "Goods"     :"text",
        "Price"     :"real",
        "Num"       :"integer",
        "Remark"    :"text",
    }


def InitBuy():
    oBugMgr = CBuyManager()
    pubdef.SetManager("buymgr", oBugMgr)
