#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

sCurPath = os.getcwd()
print(sCurPath)

sCmd = "pyinstaller -w \
--workpath D:/mycode/exe/build \
--distpath D:/mycode/exe/dist \
--specpath D:/mycode/exe \
-nGoodsManager \
-i %s/image/main.ico \
-p %s;\
%s/image;\
%s/mytool;\
C:/Python36/DLLs;\
C:/Python36/Lib \
%s/main.py"\
%(sCurPath, sCurPath, sCurPath, sCurPath, sCurPath)

os.system(sCmd)
