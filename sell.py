#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pubdef

TABLE_NAME="tbl_sell"
TABLE_CREAT_SQL="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Type text not null,
    Goods text not null,
    Seller text,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME

class CSellManager(object):
    pass

class CSell(object):
    pass

def InitBuy():
    oSellMgr = CSellManager()
    pubdef.SetManager("sellmgr", oSellMgr)
