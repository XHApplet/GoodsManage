#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtGui, QtWidgets, QtCore


class CCustomDateEdit(QtWidgets.QDateEdit):
    def __init__(self, *args):
        super(CCustomDateEdit, self).__init__(*args)
        self.setCalendarPopup(True)
        self.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)


class ExtendedComboBox(QtWidgets.QComboBox):

    MyFocusOutSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QtCore.QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())
 
        # add a completer, which uses the filter model
        self.completer = QtWidgets.QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)
 
        # connect signals
        self.lineEdit().textEdited[str].connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
 
 
    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)
 
 
    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)

    def text(self):
        return self.currentText()

    def focusOutEvent(self, e):
        self.MyFocusOutSignal.emit()
