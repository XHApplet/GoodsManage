#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mydefines
import logging

from mytool import pubdefines

TABLE_NAME="tbl_global"
TABLE_CREAT_SQL="""
create table %s
(
    GoodsList blob not null,
    GoodsType blob not null,
    GoodsInput blob not null,
    GoodsOutput blob not null
)
""" % TABLE_NAME


class CGlobalManager(object):
    ColInfo = [
        ("GoodsList", "blob"),
        ("GoodsType", "blob"),
        ("GoodsInput", "blob"),
        ("GoodsOutput", "blob"),
    ]
    def __init__(self):
        self.GoodsList = set()
        self.GoodsType = set()
        self.GoodsInput = set()
        self.GoodsOutput = set()
        self.Load()


    def Load(self):
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        # 第一次获取为空时，保存空数据到数据库
        if len(result) == 0:
            self.FristInit()
            return
        assert len(result) == 1
        result = result[0]
        assert len(result) == len(self.ColInfo)
        for iIndex, tInfo in enumerate(self.ColInfo):
            sAttr, sType = tInfo
            value = mydefines.get_value_by_data(result[iIndex], sType)
            setattr(self, sAttr, value)
            logging.debug("global:%s %s" % (sAttr, value))


    def FristInit(self):
        tData = []
        for sAttr, _ in self.ColInfo:
            value = getattr(self, sAttr)
            tData.append(value)
        sql = mydefines.get_insert_sql(TABLE_NAME, tData, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)


    def Update(self, *collist):
        lstSet = []
        for sColName, sType in self.ColInfo:
            if not sColName in collist:
                continue
            value = getattr(self, sColName)
            value = mydefines.get_insert_value(value, sType)
            lstSet.append("%s=%s" % (sColName, value))
        sSet = ",".join(lstSet)
        sql = "update %s set %s" % (TABLE_NAME, sSet)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)


    def GetAllInfoByName(self, sName):
        result = getattr(self, "Goods" + sName, None)
        assert result is not None
        return 

    def AddGoods(self, sGoods):
        self.GoodsList.add(sGoods)
        self.Update("GoodsList")

    def AddType(self, sType):
        self.GoodsType.add(sType)
        self.Update("GoodsType")

    def AddInput(self, sInput):
        """添加货物买入方向"""
        self.GoodsInput.add(sInput)
        self.Update("GoodsInput")

    def AddOutput(self, sOutput):
        """添加货物卖出方向"""
        self.GoodsOutput.add(sOutput)
        self.Update("GoodsOutput")


def InitGlobalManager():
    obj = CGlobalManager()
    pubdefines.set_manager("globalmgr", obj)
