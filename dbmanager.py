#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import logging

import globalmgr
import buy
import sell
import goods

from mytool import pubdefines


ALL_TABLES = [
    globalmgr.TABLE_CREAT_SQL,
    sell.TABLE_CREAT_SQL,
    buy.TABLE_CREAT_SQL,
    goods.TABLE_CREAT_SQL,
]

class CDBManager(object):

    DB_Name = "xh/goods.db"

    def __init__(self):
        self.Conn = None
        self.InitTable()

    def InitTable(self):
        if os.path.exists(self.DB_Name):
            return
        for sql in ALL_TABLES:
            self.Excute(sql)

    def GetConn(self):
        if not self.Conn:
            self.Conn = sqlite3.connect(self.DB_Name)
        return self.Conn

    def Excute(self, sql):
        logging.debug("ExcuteSQL:" + sql)
        coon = self.GetConn()
        cursor = coon.cursor()
        try:
            cursor.execute(sql)
            coon.commit()
        except Exception as e:
            logging.error("excute error:" + str(e))
        # coon.close()

    def Query(self, sql, bOne=False):
        logging.debug("QuerySQL:" + sql)
        coon = self.GetConn()
        cursor = coon.cursor()
        cursor.execute(sql)
        if bOne:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        # coon.close()
        return result

def InitDBManager():
    obj = CDBManager()
    pubdefines.set_manager("dbmgr", obj)
