#!/usr/bin/python3
# -*- coding: utf-8 -*-

import marshal
import binascii


def value_marshal_hex(xValue):
    sData = marshal.dumps(xValue)
    sHex = binascii.b2a_hex(sData)
    return sHex


def get_insert_value(xValue, sType):
    """通过sType类型获取对应的插入数据库的xValue的值"""
    if sType in ("int", "real", "integer"):
        return str(xValue)
    if sType in ("text", "datetime"):
        return "'%s'" % xValue
    if sType in ("blob",):
        sInfo = value_marshal_hex(xValue) 
        return "'%s'" % sInfo
    raise NotImplemented("未定义的类型:%s" % sType)


def get_insert_sql(sTableName, tData, lstColInfo):
    """
    获取插入一条信息的sql语句
    lstColInfo = [
        ("Time", "datetime"),
        ("Type", "text"),
        ("Goods", "text"),
        ("buyer", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
    ]
    """
    assert len(tData) == len(lstColInfo)
    lstKey = []
    lstValue = []
    for iIndex in range(len(tData)):
        key, sType = lstColInfo[iIndex]
        xValue = tData[iIndex]
        value = get_insert_value(xValue, sType)
        lstKey.append(key)
        lstValue.append(value)
    sKey = ",".join(lstKey)
    sValue = ",".join(lstValue)
    sql = "insert into %s(%s) values(%s)" % (sTableName, sKey, sValue)
    return sql
