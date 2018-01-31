#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pubdef

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
    pubdef.SetManager("goodsmgr", oGoodsMgr)
