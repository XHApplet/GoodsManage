#!/usr/bin/python3
# -*- coding: utf-8 -*-

import marshal
import binascii
import json
import xlwt

def value_marshal_hex(xValue):
    sData = marshal.dumps(xValue)
    sHex = binascii.b2a_hex(sData)
    sStr = sHex.decode()
    return sStr

def hex_marshal_value(sHex):
    sData = binascii.a2b_hex(sHex)
    value = marshal.loads(sData)
    return value

def get_insert_value(xValue, sType):
    """通过sType类型获取对应的插入数据库的xValue的值"""
    if sType in ("int", "real", "integer"):
        return str(xValue)
    if sType in ("text", "datetime"):
        return "'%s'" % xValue
    if sType in ("blob",):
        sStr = value_marshal_hex(xValue) 
        return "'%s'" % sStr
    raise NotImplemented("未定义的类型:%s" % sType)

def get_value_by_data(sData, sType):
    """通过数据库的的值sData和对应的插入sType,获取真实值"""
    if sType in ("int", "real", "integer", "text", "datetime"):
        return sData
    if sType in ("blob",):
        return hex_marshal_value(sData)
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
