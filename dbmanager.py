#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pubdef
import sqlite3
import buy

ALL_TABLES = [buy.TABLE_CREAT_SQL]

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
        except sqlite3.Error as e:
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
    pubdef.SetManager("dbmgr", obj)
