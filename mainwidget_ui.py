# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\Software_Goods\mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1085, 532)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWidget.setFont(font)
        MainWidget.setToolTip("")
        self.InputWidget = QtWidgets.QWidget()
        self.InputWidget.setEnabled(True)
        self.InputWidget.setObjectName("InputWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.InputWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(30, 20, 30, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonInput = QtWidgets.QPushButton(self.InputWidget)
        self.pushButtonInput.setEnabled(True)
        self.pushButtonInput.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.gridLayout.addWidget(self.pushButtonInput, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEditInputPrice = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputPrice.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputPrice.setInputMask("")
        self.lineEditInputPrice.setMaxLength(15)
        self.lineEditInputPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputPrice.setObjectName("lineEditInputPrice")
        self.gridLayout.addWidget(self.lineEditInputPrice, 2, 3, 1, 1)
        self.lineEditInputNum = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputNum.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputNum.setMaxLength(10)
        self.lineEditInputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputNum.setObjectName("lineEditInputNum")
        self.gridLayout.addWidget(self.lineEditInputNum, 2, 4, 1, 1)
        self.dateEditInput = CCustomDateEdit(self.InputWidget)
        self.dateEditInput.setMinimumSize(QtCore.QSize(0, 50))
        self.dateEditInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEditInput.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditInput.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEditInput.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditInput.setTime(QtCore.QTime(0, 0, 0))
        self.dateEditInput.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEditInput.setCalendarPopup(True)
        self.dateEditInput.setObjectName("dateEditInput")
        self.gridLayout.addWidget(self.dateEditInput, 2, 0, 1, 1)
        self.comboBoxInputGoods = ExtendedComboBox(self.InputWidget)
        self.comboBoxInputGoods.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputGoods.setFont(font)
        self.comboBoxInputGoods.setObjectName("comboBoxInputGoods")
        self.gridLayout.addWidget(self.comboBoxInputGoods, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditInputRemark = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputRemark.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputRemark.setObjectName("lineEditInputRemark")
        self.gridLayout.addWidget(self.lineEditInputRemark, 2, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.comboBoxInputType = ExtendedComboBox(self.InputWidget)
        self.comboBoxInputType.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputType.setFont(font)
        self.comboBoxInputType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxInputType.setObjectName("comboBoxInputType")
        self.gridLayout.addWidget(self.comboBoxInputType, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 2)
        self.gridLayout.setColumnMinimumWidth(2, 3)
        self.gridLayout.setColumnMinimumWidth(3, 4)
        self.gridLayout.setColumnMinimumWidth(4, 5)
        self.gridLayout.setColumnMinimumWidth(5, 6)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 2)
        self.gridLayout.setRowMinimumHeight(2, 3)
        self.gridLayout.setRowMinimumHeight(3, 4)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 6)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 3)
        self.gridLayout.setRowStretch(3, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWidget.addTab(self.InputWidget, "")
        self.OutputWidget = QtWidgets.QWidget()
        self.OutputWidget.setObjectName("OutputWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.OutputWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.comboBoxOutputBuyer = ExtendedComboBox(self.OutputWidget)
        self.comboBoxOutputBuyer.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBoxOutputBuyer.setObjectName("comboBoxOutputBuyer")
        self.gridLayout_2.addWidget(self.comboBoxOutputBuyer, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.comboBoxOutputGoods = ExtendedComboBox(self.OutputWidget)
        self.comboBoxOutputGoods.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBoxOutputGoods.setObjectName("comboBoxOutputGoods")
        self.gridLayout_2.addWidget(self.comboBoxOutputGoods, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 5, 1, 1)
        self.lineEditOutputRemark = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputRemark.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputRemark.setObjectName("lineEditOutputRemark")
        self.gridLayout_2.addWidget(self.lineEditOutputRemark, 2, 5, 1, 1)
        self.dateEditOutput = CCustomDateEdit(self.OutputWidget)
        self.dateEditOutput.setMinimumSize(QtCore.QSize(0, 50))
        self.dateEditOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditOutput.setCalendarPopup(True)
        self.dateEditOutput.setObjectName("dateEditOutput")
        self.gridLayout_2.addWidget(self.dateEditOutput, 2, 0, 1, 1)
        self.pushButtonOutput = QtWidgets.QPushButton(self.OutputWidget)
        self.pushButtonOutput.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonOutput.setObjectName("pushButtonOutput")
        self.gridLayout_2.addWidget(self.pushButtonOutput, 3, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 4, 1, 1)
        self.lineEditOutputNum = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputNum.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditOutputNum.setObjectName("lineEditOutputNum")
        self.gridLayout_2.addWidget(self.lineEditOutputNum, 2, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        self.lineEditOutputPrice = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputPrice.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditOutputPrice.setObjectName("lineEditOutputPrice")
        self.gridLayout_2.addWidget(self.lineEditOutputPrice, 2, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 4)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnStretch(4, 2)
        self.gridLayout_2.setColumnStretch(5, 6)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWidget.addTab(self.OutputWidget, "")
        self.StockWidget = QtWidgets.QWidget()
        self.StockWidget.setObjectName("StockWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.StockWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetStock = QtWidgets.QTableWidget(self.StockWidget)
        self.tableWidgetStock.setEnabled(True)
        self.tableWidgetStock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetStock.setAutoFillBackground(True)
        self.tableWidgetStock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidgetStock.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidgetStock.setLineWidth(1)
        self.tableWidgetStock.setMidLineWidth(0)
        self.tableWidgetStock.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetStock.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidgetStock.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetStock.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidgetStock.setRowCount(10)
        self.tableWidgetStock.setColumnCount(4)
        self.tableWidgetStock.setObjectName("tableWidgetStock")
        self.tableWidgetStock.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidgetStock)
        MainWidget.addTab(self.StockWidget, "")
        self.ProfitWidget = QtWidgets.QWidget()
        self.ProfitWidget.setObjectName("ProfitWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ProfitWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.ProfitWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.dateEditBegin = CCustomDateEdit(self.widget)
        self.dateEditBegin.setObjectName("dateEditBegin")
        self.horizontalLayout.addWidget(self.dateEditBegin)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.dateEditEnd = CCustomDateEdit(self.widget)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.horizontalLayout.addWidget(self.dateEditEnd)
        self.pushButtonQuery = QtWidgets.QPushButton(self.widget)
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.horizontalLayout.addWidget(self.pushButtonQuery)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.widget)
        self.tableWidgetProfile = QtWidgets.QTableWidget(self.ProfitWidget)
        self.tableWidgetProfile.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetProfile.setRowCount(0)
        self.tableWidgetProfile.setColumnCount(0)
        self.tableWidgetProfile.setObjectName("tableWidgetProfile")
        self.tableWidgetProfile.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidgetProfile)
        MainWidget.addTab(self.ProfitWidget, "")
        self.InfoWidget = QtWidgets.QWidget()
        self.InfoWidget.setObjectName("InfoWidget")
        self.pushButtonTmp = QtWidgets.QPushButton(self.InfoWidget)
        self.pushButtonTmp.setGeometry(QtCore.QRect(260, 200, 131, 61))
        self.pushButtonTmp.setObjectName("pushButtonTmp")
        MainWidget.addTab(self.InfoWidget, "")

        self.retranslateUi(MainWidget)
        MainWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)
        MainWidget.setTabOrder(self.comboBoxOutputGoods, self.comboBoxOutputBuyer)
        MainWidget.setTabOrder(self.comboBoxOutputBuyer, self.lineEditOutputPrice)
        MainWidget.setTabOrder(self.lineEditOutputPrice, self.lineEditOutputNum)
        MainWidget.setTabOrder(self.lineEditOutputNum, self.lineEditOutputRemark)
        MainWidget.setTabOrder(self.lineEditOutputRemark, self.pushButtonOutput)
        MainWidget.setTabOrder(self.pushButtonOutput, self.dateEditOutput)
        MainWidget.setTabOrder(self.dateEditOutput, self.comboBoxInputType)
        MainWidget.setTabOrder(self.comboBoxInputType, self.comboBoxInputGoods)
        MainWidget.setTabOrder(self.comboBoxInputGoods, self.lineEditInputPrice)
        MainWidget.setTabOrder(self.lineEditInputPrice, self.lineEditInputNum)
        MainWidget.setTabOrder(self.lineEditInputNum, self.lineEditInputRemark)
        MainWidget.setTabOrder(self.lineEditInputRemark, self.pushButtonInput)
        MainWidget.setTabOrder(self.pushButtonInput, self.dateEditInput)
        MainWidget.setTabOrder(self.dateEditInput, self.tableWidgetStock)
        MainWidget.setTabOrder(self.tableWidgetStock, self.dateEditBegin)
        MainWidget.setTabOrder(self.dateEditBegin, self.dateEditEnd)
        MainWidget.setTabOrder(self.dateEditEnd, self.pushButtonQuery)
        MainWidget.setTabOrder(self.pushButtonQuery, self.tableWidgetProfile)
        MainWidget.setTabOrder(self.tableWidgetProfile, self.pushButtonTmp)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "商品出入统计--肖豪"))
        self.pushButtonInput.setText(_translate("MainWidget", "确认进货"))
        self.dateEditInput.setDisplayFormat(_translate("MainWidget", "yyyy/M/d"))
        self.label_3.setText(_translate("MainWidget", "价格"))
        self.label.setText(_translate("MainWidget", "日期"))
        self.label_5.setText(_translate("MainWidget", "备注"))
        self.label_2.setText(_translate("MainWidget", "商品"))
        self.label_13.setText(_translate("MainWidget", "类别"))
        self.label_4.setText(_translate("MainWidget", "数量"))
        MainWidget.setTabText(MainWidget.indexOf(self.InputWidget), _translate("MainWidget", "进货"))
        self.label_6.setText(_translate("MainWidget", "日期"))
        self.label_8.setText(_translate("MainWidget", "买家"))
        self.label_7.setText(_translate("MainWidget", "商品"))
        self.label_11.setText(_translate("MainWidget", "备注"))
        self.pushButtonOutput.setText(_translate("MainWidget", "确认出货"))
        self.label_9.setText(_translate("MainWidget", "数量"))
        self.label_10.setText(_translate("MainWidget", "价格"))
        MainWidget.setTabText(MainWidget.indexOf(self.OutputWidget), _translate("MainWidget", "出货"))
        self.tableWidgetStock.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.StockWidget), _translate("MainWidget", "库存"))
        self.label_15.setText(_translate("MainWidget", "开始日期:"))
        self.label_16.setText(_translate("MainWidget", "结束日期:"))
        self.pushButtonQuery.setText(_translate("MainWidget", "查询"))
        self.tableWidgetProfile.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.ProfitWidget), _translate("MainWidget", "总利润"))
        self.pushButtonTmp.setText(_translate("MainWidget", "PushButton"))
        MainWidget.setTabText(MainWidget.indexOf(self.InfoWidget), _translate("MainWidget", "说明"))

from pubui import CCustomDateEdit, ExtendedComboBox
