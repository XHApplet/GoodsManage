#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
import xlwt

import mainwidget_ui

from PyQt5 import QtWidgets, QtGui, QtCore
from mytool import pubdefines


class CMyWindow(QtWidgets.QTabWidget, mainwidget_ui.Ui_MainWidget):

    def __init__(self, *args):
        super(CMyWindow, self).__init__(*args)
        self.setupUi(self)
        self.InitUI()


    def InitUI(self):
        self.InitInput()
        self.InitOutput()
        self.InitProfile()

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


    def TestQueryInput(self):
        pubdefines.call_manager_func("buymgr", "QueryAllInfo")


    def TestQueryOutput(self):
        pubdefines.call_manager_func("sellmgr", "QueryAllInfo")


    def InitConnect(self):
        self.pushButtonQueryInput.clicked.connect(self.TestQueryInput)
        self.pushButtonQueryOutput.clicked.connect(self.TestQueryOutput)
        self.pushButtonInput.clicked.connect(self.InputGoods)
        self.pushButtonOutput.clicked.connect(self.OutputGoods)
        self.currentChanged.connect(self.TabChanged)
        self.pushButtonQuery.clicked.connect(self.QueryProfile)
        self.comboBoxInputGoods.MyFocusOutSignal.connect(self.FocusOutInputGoods)
        self.pushButtonExport.clicked.connect(self.Export)


    def FocusOutInputGoods(self):
        """录入商品：当输入完商品之后自动填写类型+价格"""
        sGoods = self.comboBoxInputGoods.text()
        if not pubdefines.call_manager_func("goodsmgr", "HasGoods", sGoods):
            self.InputTiplabel.show()
            return
        self.InputTiplabel.hide()
        fPrice = pubdefines.call_manager_func("goodsmgr", "GetGoodsBuyPrice", sGoods)
        self.lineEditInputPrice.setText(str(fPrice))    # 价格自动变
        sType = pubdefines.call_manager_func("globalmgr", "GetGoodsType", sGoods)
        if sType:
            self.comboBoxInputType.setCurrentText(sType)


    def TabChanged(self, iIndex):
        """tab页改变调用"""
        if iIndex == 0:
            self.InitInput()
        if iIndex == 1:
            self.InitOutput()
        if iIndex == 2:
            self.ShowStock()
        if iIndex == 3:
            self.InitProfile()


    def InitInput(self):
        """初始化录入商品界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditInput.setDate(oCurData)
        self.comboBoxInputType.clear()
        self.comboBoxInputGoods.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllType")
        self.comboBoxInputType.addItems(lstGoodsType)
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxInputGoods.addItems(lstGoods)
        self.comboBoxInputType.setCurrentIndex(0)
        self.comboBoxInputGoods.setCurrentIndex(-1)
        self.InputTiplabel.hide()


    def InitOutput(self):
        """初始化卖出商品界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditOutput.setDate(oCurData)
        self.comboBoxOutputGoods.clear()
        self.comboBoxOutputBuyer.clear()
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxOutputGoods.addItems(lstGoods)
        lstBuyer = pubdefines.call_manager_func("globalmgr", "GetAllBuyer")
        self.comboBoxOutputBuyer.addItems(lstBuyer)
        self.comboBoxOutputGoods.setCurrentIndex(-1)
        self.comboBoxOutputBuyer.setCurrentIndex(-1)


    def InitProfile(self):
        """初始化利润界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditEnd.setDate(oCurData)
        self.dateEditBegin.setDate(oCurData.addMonths(-1))


    def slotInformation(self, sMsg, sTitle="提示"):
        QtWidgets.QMessageBox.information(self, sTitle, self.tr(sMsg))  


    def ValidInput(self):
        """录入商品时控件判断"""
        if not self.lineEditInputPrice.text():
            self.slotInformation("价格不能为空")
            return False
        if not self.lineEditInputNum.text():
            self.slotInformation("数量不能为空")
            return False
        if not self.dateEditInput.dateTime():
            self.slotInformation("日期不能为空")
            return False
        if not self.comboBoxInputType.currentText():
            self.slotInformation("类别不能为空")
            return False
        if not self.comboBoxInputGoods.currentText():
            self.slotInformation("商品不能为空")
            return False
        return True


    def InputGoods(self):
        """点击录入商品调用"""
        if not self.ValidInput():
            return
        self.dateEditInput.setTime(QtCore.QTime.currentTime())
        oDataTime = self.dateEditInput.dateTime()
        iTime = oDataTime.toTime_t()
        sGoodsType = self.comboBoxInputType.currentText()
        sGoods = self.comboBoxInputGoods.currentText()
        fPrice = float(self.lineEditInputPrice.text())
        iNum = int(self.lineEditInputNum.text())
        sRemark = self.lineEditInputRemark.text()

        # TODO 判断是否已经有了.增加商品、价格判断
        tInfo = (iTime, sGoodsType, sGoods, fPrice, iNum, sRemark)
        logging.info("InputGoods:%s" % (tInfo,))
        pubdefines.call_manager_func("buymgr", "InputGoods", tInfo)
        pubdefines.call_manager_func("goodsmgr", "InputGoods", sGoods, fPrice, iNum)

        if not pubdefines.call_manager_func("globalmgr", "HasGoods", sGoods):
            pubdefines.call_manager_func("globalmgr", "AddGoods", sGoodsType, sGoods)
        
        self.InitInput()


    def ValidOutput(self):
        """卖出商品时控件判断"""
        if not self.lineEditOutputPrice.text():
            self.slotInformation("价格不能为空")
            return False
        if not self.lineEditOutputNum.text():
            self.slotInformation("数量不能为空")
            return False
        if not self.dateEditOutput.dateTime():
            self.slotInformation("日期不能为空")
            return False
        if not self.comboBoxOutputBuyer.currentText():
            self.slotInformation("买家不能为空")
            return False
        if not self.comboBoxOutputGoods.currentText():
            self.slotInformation("商品不能为空")
            return False
        sGoods = self.comboBoxOutputGoods.text()
        if not pubdefines.call_manager_func("goodsmgr", "HasGoods", sGoods):
            self.slotInformation("库存中无商品记录")
            return False
        iStock = pubdefines.call_manager_func("goodsmgr", "GetGoodsNum", sGoods)
        iNum = int(self.lineEditOutputNum.text())
        if iStock < iNum:
            self.slotInformation("没有足够的库存,当前库存%s" % iStock)
            return False
        return True


    def OutputGoods(self):
        if not self.ValidOutput():
            return
        self.dateEditOutput.setTime(QtCore.QTime.currentTime())
        oDataTime = self.dateEditOutput.dateTime()
        iTime = oDataTime.toTime_t()
        sGoods = self.comboBoxOutputGoods.currentText()
        sBuyer = self.comboBoxOutputBuyer.currentText()
        fPrice = float(self.lineEditOutputPrice.text())
        iNum = int(self.lineEditOutputNum.text())
        sRemark = self.lineEditOutputRemark.text()

        tInfo = [iTime, sGoods, sBuyer, fPrice, iNum, sRemark]
        logging.info("OutputGoods:%s" % (tInfo,))

        # 计算本次卖出的利润为多少
        fProfile = pubdefines.call_manager_func("goodsmgr", "OutputGoods", sGoods, fPrice, iNum)
        assert fProfile is not None

        tInfo.append(fProfile)
        pubdefines.call_manager_func("sellmgr", "OutputGoods", tInfo)
        pubdefines.call_manager_func("globalmgr", "AddBuyer", sBuyer)

        self.InitOutput()


    def ShowStock(self):
        lstTitle = ["商品", "当前买入价格", "当前卖出价格", "库存"]
        self.tableWidgetStock.setHorizontalHeaderLabels(lstTitle)
        dGoodsInfo = pubdefines.call_manager_func("goodsmgr", "GetGoodsInfo")
        iGoodsNum = len(dGoodsInfo)
        self.tableWidgetStock.setRowCount(iGoodsNum)

        self.tableWidgetStock.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置每列自适应
        # self.tableWidgetStock.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        iIndex = 0
        for sGoods, tInfo in dGoodsInfo.items():
            item = QtWidgets.QTableWidgetItem(str(sGoods))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetStock.setItem(iIndex, 0, item)
            for y in range(len(tInfo) - 1):
                # TODO 其他类型怎么判断,字符串价格排序有问题
                xTmp = tInfo[y]
                item = QtWidgets.QTableWidgetItem(str(xTmp))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetStock.setItem(iIndex, y + 1, item)
            iIndex += 1


    def QueryProfile(self):
        """查询利润"""
        oBeginDate = self.dateEditBegin.date()
        sBeginTime = oBeginDate.toString("yyyy-MM-dd 00:00:00")
        iBeginTime = pubdefines.str_to_time(sBeginTime)
        oEndDate = self.dateEditEnd.date()
        sEndTime = oEndDate.toString("yyyy-MM-dd 23:59:59")
        iEndTime = pubdefines.str_to_time(sEndTime)
        self.MaxProfileCol = 0
        dSellInfo = pubdefines.call_manager_func("sellmgr", "GetSellInfo", iBeginTime, iEndTime)
        self.ProfileInfo = {}
        for _, tSellInfo in dSellInfo.items():
            iTime = tSellInfo[0]
            sTime = pubdefines.time_to_str(iTime)
            sGoods = tSellInfo[1]
            fProfile = tSellInfo[6]
            
            sDayTime = sTime[:10]
            sMonthTime = sTime[:7]
            sYearTime = sTime[:4]
            self.AddProfile(sGoods, sDayTime, fProfile)
            self.AddProfile(sGoods, sMonthTime, fProfile)
            self.AddProfile(sGoods, sYearTime, fProfile)
            self.AddProfile(sGoods, "总利润", fProfile)

        iGoodsNum = len(self.ProfileInfo)
        self.tableWidgetProfile.setRowCount(iGoodsNum)
        
        lstTime = ["总利润",]
        while oBeginDate.toString("yyyy-MM") <= oEndDate.toString("yyyy-MM"):
            lstTime.append(oBeginDate.toString("yyyy-MM"))
            oBeginDate = oBeginDate.addMonths(1)

        self.tableWidgetProfile.setColumnCount(len(lstTime) + 1 )

        lstGoods = [ sGoods for sGoods in self.ProfileInfo ]

        lstTitle = lstTime[:]
        lstTitle.insert(0, "商品")
        self.tableWidgetProfile.setHorizontalHeaderLabels(lstTitle)
        if len(lstTime) < 14:
            self.tableWidgetProfile.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        for iRow, sGoods in enumerate(lstGoods):
            item = QtWidgets.QTableWidgetItem(sGoods)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetProfile.setItem(iRow, 0, item)
            for iCol, sTime in enumerate(lstTime):
                fProfile = self.GetProfileByDate(sGoods, sTime)
                item = QtWidgets.QTableWidgetItem(str(fProfile))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetProfile.setItem(iRow, iCol + 1, item)


    def GetProfileByDate(self, sGoods, sTimeKey):
        if not sGoods in self.ProfileInfo:
            return ""
        if not sTimeKey in self.ProfileInfo[sGoods]:
            return ""
        return self.ProfileInfo[sGoods][sTimeKey]


    def AddProfile(self, sGoods, sTimeKey, fProfile):
        if not sGoods in self.ProfileInfo:
            self.ProfileInfo[sGoods] = {}
        if not sTimeKey in self.ProfileInfo[sGoods]:
            self.ProfileInfo[sGoods][sTimeKey] = 0
        self.ProfileInfo[sGoods][sTimeKey] += fProfile


    def Export(self):
        sFileName = QtWidgets.QFileDialog.getSaveFileName(self, "保存表格", "", ".xls(*.xls)")[0]
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", True)
        self.Write2Sheet(sheet)
        wbk.save(sFileName)


    def Write2Sheet(self, sheet):
        iRow = self.tableWidgetProfile.rowCount()
        iCol = self.tableWidgetProfile.columnCount()
        for col in range(iCol):
            oItem = self.tableWidgetProfile.horizontalHeaderItem(col)
            text = str(oItem.text())
            sheet.write(0, col, text)
        for row in range(iRow):
            for col in range(iCol):
                oItem = self.tableWidgetProfile.item(row, col)
                text = ""
                if oItem:
                    text = str(oItem.text())
                sheet.write(row + 1, col, text)



def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
