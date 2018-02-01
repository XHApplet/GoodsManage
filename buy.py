#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    buyer text,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME

class CBuyManager(object):

    ColInfo = [
        ("Time", "datetime"),
        ("Type", "text"),
        ("Goods", "text"),
        ("buyer", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
    ]
    AutoInfo = ("ID", "integer")

    def __init__(self):
        self.BuyInfo = {}

    def InputGoods(self, tData):
        sql = mydefines.get_insert_sql(TABLE_NAME, tData, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def QueryAllInfo(self):
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for tmp in result:
            print(tmp)

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
