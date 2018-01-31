#!/usr/bin/python3
# -*- coding: utf-8 -*-

if "g_Manager" not in globals():
    g_Manager = {}

def SetManager(sFlag, obj):
    global g_Manager
    g_Manager[sFlag] = obj

def GetManager(sFlag):
    global g_Manager
    obj = g_Manager.get(sFlag, None)
    return obj

def CallManagerFunc(sFlag, sFunc, *args):
    obj = GetManager(sFlag)
    func = getattr(obj, sFunc)
    if not func:
        return None
    result = func(*args)
    return result

