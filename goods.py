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
    Num integer not null,
    NumInfo blob not null
)
""" % TABLE_NAME


class CGoodsManager(object):

    ColInfo = [
        ("Goods", "text"),
        ("BuyPrice", "integer"),
        ("SellPrice", "integer"),
        ("Num", "integer"),
        ("NumInfo", "blob"),
    ]
    KeyNum = 1

    def __init__(self):
        self.GoodsInfo = {}
        self.Load()


    def HasGoods(self, sGood):
        if sGood in self.GoodsInfo:
            return True
        return False


    def GetGoodsInfo(self):
        return self.GoodsInfo


    def GetGoodsNum(self, sGoods):
        tInfo = self.GoodsInfo.get(sGoods, None)
        assert tInfo is not None
        return tInfo[2]


    def GetGoodsBuyPrice(self, sGoods):
        tInfo = self.GoodsInfo.get(sGoods, None)
        assert tInfo is not None
        return tInfo[0]


    def GetGoodsSellPrice(self, sGoods):
        tInfo = self.GoodsInfo.get(sGoods, None)
        assert tInfo is not None
        return tInfo[1]


    def InputGoods(self, sGoods, fBuyPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.NewGoodsInfo(sGoods)
        tInfo = self.GoodsInfo[sGoods]
        tInfo[0] = fBuyPrice
        tInfo[2] += iNum
        self.Add2NumInfo(tInfo[3], fBuyPrice, iNum)
        self.Update(sGoods, tInfo)


    def Add2NumInfo(self, lstNumInfo, fBuyPrice, iNum):
        if not lstNumInfo:
            lstNumInfo.append([fBuyPrice, iNum])
            return
        fLastPrice, iNowNum = lstNumInfo[-1]
        if abs(fLastPrice - fBuyPrice) < 1e-6:  #与上次价格相同
            lstNumInfo[-1][1] = iNowNum + iNum
        else:   #与上次价格不同
            lstNumInfo.append([fBuyPrice, iNum])


    def OutputGoods(self, sGoods, fSellPrice, iNum):
        if not sGoods in self.GoodsInfo:
            self.NewGoodsInfo(sGoods)
        tInfo = self.GoodsInfo[sGoods]
        tInfo[1] = fSellPrice
        if tInfo[2] < iNum:
            logging.error("%s 库存:%s 卖出:%s" % (sGoods, tInfo[2], iNum))
            return
        tInfo[2] -= iNum
        fProfile = self.Del4NumInfo(tInfo[3], fSellPrice, iNum)
        self.Update(sGoods, tInfo)
        return fProfile


    def Del4NumInfo(self, lstNumInfo, fSellPrice, iNum):
        fProfile = 0
        while lstNumInfo:
            fBuyPrice, iStockNum = lstNumInfo.pop(0)
            if iStockNum > iNum:
                fProfile = fProfile + (fSellPrice - fBuyPrice) * iNum
                lstNumInfo.insert(0, [fBuyPrice, iStockNum - iNum])
                return fProfile
            if iStockNum == iNum:
                fProfile = fProfile + (fSellPrice - fBuyPrice) * iNum
                return fProfile
            iNum = iNum - iStockNum
            fProfile = fProfile + (fSellPrice - fBuyPrice) * iStockNum
        return fProfile


    def NewGoodsInfo(self, sGoods):
        self.GoodsInfo[sGoods] = [0, 0, 0, []]
        sql = mydefines.get_insert_sql(TABLE_NAME, [sGoods, *self.GoodsInfo[sGoods]], self.ColInfo)
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
            tInfo[3] = mydefines.get_value_by_data(tInfo[3], "blob")
            self.GoodsInfo[sGoods] = tInfo
            logging.debug("load: %s %s" % (sGoods, tInfo))
        logging.info("    load finish %s" % len(result))



def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
