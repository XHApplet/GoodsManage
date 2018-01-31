#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import goods
import buy
import dbmanager

import mainwidget

def InitManager():
    goods.InitGoods()
    buy.InitBuy()
    dbmanager.InitDBManager()

def InitUI():
    mainwidget.InitMainWidget()

def Start():
    InitManager()
    InitUI()

if __name__ == "__main__":
    Start()

