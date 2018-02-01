#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pubdef

TABLE_NAME="tbl_global"
TABLE_CREAT_SQL="""
create table %s
(
    Goods blob not null,
    Type blob not null,
    Input blob not null,
    Output blob not null
)
""" % TABLE_NAME


class CGlobalManager(object):
    def __init__(self):
        self.GoodsList = set()
        self.GoodsType = set()
        self.GoodsInput = set()
        self.GoodsOutput = set()

    def Load(self, dInfo):
        sql = "select * from %s" % TABLE_NAME
        result = pubdef.CallManagerFunc("dbmgr", "Query", sql)
        # 第一次获取为空时，保存空数据到数据库
        if len(result) == 0:
            self.SaveAll()
            return
        assert len(result) == 1
        self.GoodsList, self.GoodsType, self.GoodsInput, self.GoodsOutput = result[0]

    def SaveAll(self):
        pass

    def Save(self):
        pass

    def AddGoods(self, sGoods):
        self.GoodsList.add(sGoods)

    def AddType(self, sType):
        self.GoodsType.add(sType)

    def AddInput(self, sInput):
        """添加货物买入方向"""
        self.GoodsInput.add(sInput)

    def AddOutput(self, sOutput):
        """添加货物卖出方向"""
        self.GoodsOutput.add(sOutput)

    def GetGoodsName(self):
        return [ sName for sName in self.GoodsInfo ]



class CGoods(object):
    pass


def InitGoods():
    obj = CGlobalManager()
    pubdef.SetManager("globalmgr", obj)
