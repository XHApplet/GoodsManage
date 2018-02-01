#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import dbmanager
import buy
import sell
import goods

import mainwidget

def InitManager():
    dbmanager.InitDBManager()
    buy.InitBuy()
    sell.InitSell()
    goods.InitGoods()

def InitUI():
    mainwidget.InitMainWidget()

def Start():
    InitManager()
    InitUI()

if __name__ == "__main__":
    Start()

