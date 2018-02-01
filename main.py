#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import logging

import dbmanager
import buy
import sell
import goods

import mainwidget

from mytool import pubdefines

def InitConfig():
    sLogDir = os.path.join(os.getcwd(), "log")
    pubdefines.makedirs(sLogDir)
    logging.basicConfig(
        filename = "log/log%s.log" % pubdefines.time_to_str(timeformat="%Y-%m-%d %H-%M-%S"),
        format = "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        level = logging.DEBUG,
    )
    ch = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(ch)
    logging.info("init config...")


def InitManager():
    dbmanager.InitDBManager()
    buy.InitBuy()
    sell.InitSell()
    goods.InitGoods()
    logging.info("init manager...")


def InitUI():
    logging.info("init ui...")
    mainwidget.InitMainWidget()

def Start():
    InitConfig()
    InitManager()
    InitUI()

if __name__ == "__main__":
    Start()

