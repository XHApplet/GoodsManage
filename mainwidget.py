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
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.InitControl()
        self.InitInput()
        self.InitOutput()
        self.InitControl()
        self.InitConnect()
        self.show()

    def InitControl(self):
        """初始化控件+限制"""
        tRegExp = QtCore.QRegExp("^(-?\d+)(\.\d+)?$")
        self.ValidatorPrice = QtGui.QRegExpValidator(tRegExp)
        self.ValidatorNum = QtGui.QIntValidator(1, 999999)

        self.lineEditInputPrice.setValidator(self.ValidatorPrice)
        self.lineEditInputNum.setValidator(self.ValidatorNum)
        self.lineEditOutputPrice.setValidator(self.ValidatorPrice)
        self.lineEditOutputNum.setValidator(self.ValidatorNum)


    def InitConnect(self):
        self.pushButtonTmp.clicked.connect(self.TestOP)
        self.pushButtonInput.clicked.connect(self.InputGoods)
        self.pushButtonOutput.clicked.connect(self.OutputGoods)
        self.currentChanged.connect(self.TabChanged)
        self.pushButtonQuery.clicked.connect(self.QueryProfile)


    def TabChanged(self, iIndex):
        if iIndex == 0:
            self.InitInput()
        if iIndex == 1:
            self.InitOutput()
        if iIndex == 2:
            self.ShowStock()
        if iIndex == 3:
            self.InitProfile()


    def InitInput(self):
        oCurData = QtCore.QDate.currentDate()
        self.dateEditInput.setDate(oCurData)
        self.comboBoxInputType.clear()
        self.comboBoxInputGoods.clear()
        self.comboBoxInputBuyer.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "Type")
        self.comboBoxInputType.addItems(lstGoodsType)
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "List")
        self.comboBoxInputGoods.addItems(lstGoods)
        lstOutput = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "Output")
        self.comboBoxInputBuyer.addItems(lstOutput)
        self.comboBoxInputType.setCurrentText("")
        self.comboBoxInputGoods.setCurrentText("")
        self.comboBoxInputBuyer.setCurrentText("")


    def InitOutput(self):
        oCurData = QtCore.QDate.currentDate()
        self.dateEditOutput.setDate(oCurData)
        self.comboBoxOutputType.clear()
        self.comboBoxOutputGoods.clear()
        self.comboBoxOutputSeller.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "Type")
        self.comboBoxOutputType.addItems(lstGoodsType)
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "List")
        self.comboBoxOutputGoods.addItems(lstGoods)
        lstOutput = pubdefines.call_manager_func("globalmgr", "GetAllInfoByName", "Output")
        self.comboBoxOutputSeller.addItems(lstOutput)
        self.comboBoxOutputType.setCurrentText("")
        self.comboBoxOutputGoods.setCurrentText("")
        self.comboBoxOutputSeller.setCurrentText("")


    def InitProfile(self):
        oCurData = QtCore.QDate.currentDate()
        self.dateEditEnd.setDate(oCurData)
        self.dateEditBegin.setDate(oCurData.addMonths(-1))

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
        oData = self.dateEditInput.dateTime()
        sData = oData.toString("yyyy-MM-dd hh:mm:ss")
        sGoodsType = self.comboBoxInputType.currentText()
        sGoods = self.comboBoxInputGoods.currentText()
        sBuyer = self.comboBoxInputBuyer.currentText()
        fPrice = float(self.lineEditInputPrice.text())
        iNum = int(self.lineEditInputNum.text())
        sRemark = self.lineEditInputRemark.text()

        tInfo = (sData, sGoodsType, sGoods, sBuyer, fPrice, iNum, sRemark)
        logging.debug("InputGoods:%s" % (tInfo,))

        pubdefines.call_manager_func("buymgr", "InputGoods", tInfo)
        pubdefines.call_manager_func("goodsmgr", "InputGoods", sGoods, fPrice, iNum)
        # TODO 判断是否已经有了.增加商品、价格判断
        pubdefines.call_manager_func("globalmgr", "AddGoods", sGoods)
        pubdefines.call_manager_func("globalmgr", "AddGoodsType", sGoodsType)
        pubdefines.call_manager_func("globalmgr", "AddBuyer", sBuyer)

    def OutputGoods(self):
        self.dateEditOutput.setTime(QtCore.QTime.currentTime())
        oData = self.dateEditOutput.dateTime()
        sData = oData.toString("yyyy-MM-dd hh:mm:ss")
        sGoodsType = self.comboBoxOutputType.currentText()
        sGoods = self.comboBoxOutputGoods.currentText()
        sSeller = self.comboBoxOutputSeller.currentText()
        fPrice = float(self.lineEditOutputPrice.text())
        iNum = int(self.lineEditOutputNum.text())
        sRemark = self.lineEditOutputRemark.text()

        tInfo = (sData, sGoodsType, sGoods, sSeller, fPrice, iNum, sRemark)
        logging.debug("OutputGoods:%s" % (tInfo,))

        pubdefines.call_manager_func("sellmgr", "OutputGoods", tInfo)
        pubdefines.call_manager_func("goodsmgr", "OutputGoods", sGoods, fPrice, iNum)
        # TODO 判断是否已经有了.增加商品、价格判断
        pubdefines.call_manager_func("globalmgr", "AddGoods", sGoods)
        pubdefines.call_manager_func("globalmgr", "AddGoodsType", sGoodsType)
        pubdefines.call_manager_func("globalmgr", "AddSeller", sSeller)


    def ShowStock(self):
        lstTitle = ["商品", "当前买入价格", "当前卖出价格", "库存"]
        self.tableWidgetStock.setHorizontalHeaderLabels(lstTitle)
        dGoodsInfo = pubdefines.call_manager_func("goodsmgr", "GetGoodsInfo")
        iGoodsNum = len(dGoodsInfo)
        self.tableWidgetStock.setRowCount(iGoodsNum)

        iIndex = 0
        for sGoods, tInfo in dGoodsInfo.items():
            item = QtWidgets.QTableWidgetItem(str(sGoods))
            self.tableWidgetStock.setItem(iIndex, 0, item)
            for y, tmp in enumerate(tInfo):
                # TODO 其他类型怎么判断
                item = QtWidgets.QTableWidgetItem(str(tmp))
                self.tableWidgetStock.setItem(iIndex, y + 1, item)
            iIndex += 1


    def QueryProfile(self):
        sBegin = self.dateEditBegin.date().toString("yyyy-MM-dd")
        sEnd = self.dateEditEnd.date().toString("yyyy-MM-dd")
        print("begin", sBegin, sEnd)



def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
