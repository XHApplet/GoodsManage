#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mytool import pubdefines

TABLE_NAME="tbl_buy"
TABLE_CREAT_SQL="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Type text not null,
    Goods text not null,
    buyer text,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME

class CBuyManager(object):
    def __init__(self):
        self.BuyInfo = {}

    def InputGoods(self, data, sType, sGoods, fPrice, iNum, sRemark):
        sql = "insert into %s(Time, Type, Goods, Price, Num, Remark) values('%s', '%s', %s, %s, '%s')" % (TABLE_NAME,
            data, sType, sGoods, fPrice, iNum, sRemark)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def Query(self):
        pass

# class CBuy(object):
#     ColType = {
#         "Time"      :"time",
#         "Goods"     :"text",
#         "Price"     :"real",
#         "Num"       :"integer",
#         "Remark"    :"text",
#     }


def InitBuy():
    oBugMgr = CBuyManager()
    pubdefines.set_manager("buymgr", oBugMgr)
