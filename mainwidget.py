#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import mainwidget_ui
from mytool import pubdefines

from PyQt5 import QtWidgets, QtGui, QtCore

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
        return True

    def InputGoods(self):
        if not self.ValidInput():
            return
        self.dateEditInput.setTime(QtCore.QTime.currentTime())
        sData = self.dateEditInput.dateTime()
        sGoods = self.comboBoxInputType.currentText()
        fPrice = float(self.lineEditInputPrice.text())
        iNum = int(self.lineEditInputNum.text())
        sRemark = self.lineEditInputRemark.text()
        print("InputGoods-%s-%s-%s-%s-%s" % (sData, sGoods, fPrice, iNum, sRemark))
        pubdefines.call_manager_func("buymgr", "InputGoods", sData, sGoods, fPrice, iNum, sRemark)

def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
