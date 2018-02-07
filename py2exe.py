#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

sCurPath = os.getcwd()
print(sCurPath)

sCmd = "pyinstaller -w \
--specpath D:/mycode/exe \
-p D:/mycode/exe \
-nxiaohao \
-i %s/image/main.ico \
-p %s;\
%s/mytool;\
C:/Python36/DLLs;\
C:/Python36/Lib \
%s/main.py"\
%(sCurPath, sCurPath, sCurPath, sCurPath)

os.system(sCmd)
