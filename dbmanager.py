#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mytool import pubdefines
import sqlite3
import globalmgr
import buy
import sell
import goods

ALL_TABLES = [
    globalmgr.TABLE_CREAT_SQL,
    sell.TABLE_CREAT_SQL,
    buy.TABLE_CREAT_SQL,
    goods.TABLE_CREAT_SQL,
]

class CDBManager(object):

    DB_Name = "goods.db"

    def __init__(self):
        self.Conn = None
        self.InitTable()

    def InitTable(self):
        for sql in ALL_TABLES:
            sResult = self.Excute(sql)

    def GetConn(self):
        if not self.Conn:
            self.Conn = sqlite3.connect(self.DB_Name)
        return self.Conn

    def Excute(self, sql):
        print(sql)
        coon = self.GetConn()
        cursor = coon.cursor()
        try:
            cursor.execute(sql)
            coon.commit()
        except Exception as e:
            # TODO
            print(e)
            return e.args[0]
        # coon.close()
        return True

    def Query(self, sql):
        coon = self.GetConn()
        cursor = coon.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # coon.close()
        return result

def InitDBManager():
    obj = CDBManager()
    pubdefines.set_manager("dbmgr", obj)
