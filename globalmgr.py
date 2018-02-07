#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mydefines
import logging

from mytool import pubdefines

TABLE_NAME="tbl_global"
TABLE_CREAT_SQL="""
create table %s
(
    Name text not null PRIMARY KEY,
    Data blob not null
)
""" % TABLE_NAME


class CGlobalManager(object):
    ColInfo = [
        ("Name", "text"),
        ("Data", "blob"),
    ]
    NameList = ["GoodsInfo", "Buyer", "GoodsType"]
    FilterInfo = {
        "（" :"(",
        "）" :")",
        "\t" :"",
        "\n" :"",
    }

    def __init__(self):
        self.GoodsInfo = {}
        self.GoodsType = set({"公司", "非公司", "自制"})
        self.Buyer = set()
        self.LoadFromDB()
        # self.LoadFromConfig()


    def FilterGoods(self, sGoods):
        for old, new in self.FilterInfo.items():
            sGoods = sGoods.replace(old, new)
        return sGoods


    def LoadFromDB(self):
        for sAttr in self.NameList:
            sql = "select * from %s where Name='%s'" % (TABLE_NAME, sAttr)
            result = pubdefines.call_manager_func("dbmgr", "Query", sql, True)
            if not result:
                self.FirstInsertData(sAttr)
                continue
            assert len(result) == 2
            _, sData = result
            value = mydefines.get_value_by_data(sData, "blob")
            setattr(self, sAttr, value)


    def FirstInsertData(self, sAttr):
        value = getattr(self, sAttr, None)
        assert value is not None
        value = mydefines.get_insert_value(value, "blob")
        sql = "insert into %s values('%s', %s)" % (TABLE_NAME, sAttr, value)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)


    def LoadFromConfig(self):
        tGoodsList = set()
        with open("config/goods.txt", "r+", encoding="utf8") as fg:
            lstGoods = fg.readlines()
            for sGoods in lstGoods:
                sGoods = self.FilterGoods(sGoods)
                self.GoodsInfo.add(sGoods)
        with open("config/output.txt", "r+", encoding="utf8") as fo:
            lstOutput = fo.readlines()
            for sOutput in lstOutput:
                sOutput = self.FilterGoods(sOutput)
                self.GoodsOutput.add(sOutput)
        self.UpdateAll()


    def UpdateAll(self, sAttr):
        value = getattr(self, sAttr, None)
        assert value is not None
        value = mydefines.get_insert_value(value, "blob")
        sql = "update %s set Data=%s where Name='%s'" % (TABLE_NAME, value, sAttr)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)


    def GetAllGoodsList(self):
        return [ sGoods for sGoods in self.GoodsInfo ]


    def GetAllType(self):
        return self.GoodsType


    def GetAllBuyer(self):
        return self.Buyer


    def GetGoodsType(self, sGoods):
        sType = self.GoodsInfo.get(sGoods, None)
        return sType


    def HasGoods(self, sGoods):
        if sGoods in self.GoodsInfo:
            return True
        return False


    def AddGoods(self, sGoodsType, sGoods):
        """添加商品以及类型"""
        if self.HasGoods(sGoods):
            return
        self.GoodsInfo[sGoods] = sGoodsType
        self.UpdateAll("GoodsInfo")


    def HasBuyer(self, sBuyer):
        if sBuyer in self.Buyer:
            return True
        return False


    def AddBuyer(self, sBuyer):
        """添加买家方向"""
        if self.HasBuyer(sBuyer):
            return
        self.Buyer.add(sBuyer)
        self.UpdateAll("Buyer")




def InitGlobalManager():
    obj = CGlobalManager()
    pubdefines.set_manager("globalmgr", obj)
