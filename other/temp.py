#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

class CMY(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.Init()

    def Init(self):
        self.addTab(QtWidgets.QFrame(self), "1")
        self.addTab(QtWidgets.QFrame(self), "2")
        self.currentChanged.connect(self.Test)

    def Test(self, *args):
        print(args)

app = QtWidgets.QApplication(sys.argv)
love = CMY()
love.show()
sys.exit(app.exec_())