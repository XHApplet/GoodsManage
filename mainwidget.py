#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging

import mainwidget_ui

from PyQt5 import QtWidgets, QtGui, QtCore
from mytool import pubdefines


class CMyWindow(QtWidgets.QTabWidget, mainwidget_ui.Ui_MainWidget):
    def __init__(self, *args):
        super(CMyWindow, self).__init__(*args)
        self.TestItems = ["love", "7.25大理石锯条", "300电镀异", "10公分干抛片(闵)", "8.1米成品锯条", "麻石定厚刀头"]
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.num = 0
        self.InitControl()
        self.InitConnect()
        self.show()

    def InitControl(self):
        """初始化控件+限制"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditInput.setDate(oCurData)
        self.dateEditOutput.setDate(oCurData)

        self.comboBoxInputType.addItems(self.TestItems)
        self.comboBoxOutputType.addItems(self.TestItems)
        self.comboBoxInputGoods.addItems(self.TestItems)
        self.comboBoxOutputGoods.addItems(self.TestItems)
        self.comboBoxInputBuyer.addItems(self.TestItems)
        self.comboBoxOutputSeller.addItems(self.TestItems)

        self.comboBoxInputType.setCurrentText("")

        tRegExp = QtCore.QRegExp("^(-?\d+)(\.\d+)?$")
        self.ValidatorPrice = QtGui.QRegExpValidator(tRegExp)
        self.ValidatorNum = QtGui.QIntValidator(1, 999999)

        self.lineEditInputPrice.setValidator(self.ValidatorPrice)
        self.lineEditInputNum.setValidator(self.ValidatorNum)
        self.lineEditOutpuPrice.setValidator(self.ValidatorPrice)
        self.lineEditOutputNum.setValidator(self.ValidatorNum)


    def InitConnect(self):
        self.pushButtonInput.clicked.connect(self.InputGoods)
        self.pushButtonTmp.clicked.connect(self.TestOP)

    def TestOP(self):
        pubdefines.call_manager_func("buymgr", "QueryAllInfo")

    def ValidInput(self):
        if not self.lineEditInputPrice.text():
            self.lineEditInputPrice.setPlaceholderText("价格不能为空")
            return False
        if not self.lineEditInputNum.text():
            self.lineEditInputNum.setPlaceholderText("数量不能为空")
            return False
        if not self.dateEditInput.dateTime():
            return False
        if not self.comboBoxInputType.currentText():
            return False
        if not self.comboBoxInputGoods.currentText():
            return False
        if not self.comboBoxInputBuyer.currentText():
            return False
        return True

    def InputGoods(self):
        if not self.ValidInput():
            return
        self.dateEditInput.setTime(QtCore.QTime.currentTime())
        sData = self.dateEditInput.dateTime()
        sType = self.comboBoxInputType.currentText()
        sGoods = self.comboBoxInputType.currentText()
        sBuyer = self.comboBoxInputBuyer.currentText()
        fPrice = float(self.lineEditInputPrice.text())
        iNum = int(self.lineEditInputNum.text())
        sRemark = self.lineEditInputRemark.text()

        # TODO增加商品、价格判断
        tInfo = (sData, sType, sGoods, sBuyer, fPrice, iNum, sRemark)
        logging.debug("InputGoods-%s" % (tInfo,))
        pubdefines.call_manager_func("buymgr", "InputGoods", tInfo)

def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
