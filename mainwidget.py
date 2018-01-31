#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import mainwidget_ui
import pubdef

from PyQt5 import QtWidgets, QtGui, QtCore

class CMyWindow(QtWidgets.QTabWidget, mainwidget_ui.Ui_MainWidget):
    def __init__(self, *args):
        super(CMyWindow, self).__init__(*args)
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.num = 0
        self.InitControl()
        self.InitConnect()
        self.show()

    def InitControl(self):
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEditOutput.setDate(QtCore.QDate.currentDate())
        self.comboBoxType.addItems(["xiao hao", 'hola muchachos', 'adios amigos', 'hello world', 'good bye'])
        self.comboBoxType.setCurrentText("")
        tRegExp = QtCore.QRegExp("^(-?\d+)(\.\d+)?$")
        tValidator = QtGui.QRegExpValidator(tRegExp)
        self.lineEditPrice.setValidator(tValidator)
        self.lineEditNum.setValidator(QtGui.QIntValidator(1, 999999))

    def InitConnect(self):
        self.ConfirmButton.clicked.connect(self.InputGoods)

    def ValidInput(self):
        if not self.lineEditPrice.text():
            self.lineEditPrice.setPlaceholderText("价格不能为空")
            return False
        if not self.lineEditNum.text():
            self.lineEditNum.setPlaceholderText("数量不能为空")
            return False
        if not self.dateEdit.dateTime():
            return False
        if not self.comboBoxType.currentText():
            return False
        return True

    def InputGoods(self):
        if not self.ValidInput():
            return
        self.dateEdit.setTime(QtCore.QTime.currentTime())
        sData = self.dateEdit.dateTime()
        sGoods = self.comboBoxType.currentText()
        fPrice = float(self.lineEditPrice.text())
        iNum = int(self.lineEditNum.text())
        sRemark = self.lineEditRemark.text()
        print("InputGoods-%s-%s-%s-%s-%s" % (sData, sGoods, fPrice, iNum, sRemark))
        pubdef.CallManagerFunc("buymgr", "InputGoods", sData, sGoods, fPrice, iNum, sRemark)

def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())

