# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmSpatialIndex.ui'
#
# Created: Wed Jul 29 01:08:22 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(351, 272)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkExternalFiles = QtGui.QCheckBox(Dialog)
        self.chkExternalFiles.setObjectName(_fromUtf8("chkExternalFiles"))
        self.horizontalLayout.addWidget(self.chkExternalFiles)
        self.btnSelectFiles = QtGui.QPushButton(Dialog)
        self.btnSelectFiles.setObjectName(_fromUtf8("btnSelectFiles"))
        self.horizontalLayout.addWidget(self.btnSelectFiles)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lstLayers = QtGui.QListWidget(Dialog)
        self.lstLayers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstLayers.setAlternatingRowColors(True)
        self.lstLayers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lstLayers.setObjectName(_fromUtf8("lstLayers"))
        self.verticalLayout.addWidget(self.lstLayers)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnSelectAll = QtGui.QPushButton(Dialog)
        self.btnSelectAll.setObjectName(_fromUtf8("btnSelectAll"))
        self.horizontalLayout_2.addWidget(self.btnSelectAll)
        self.btnSelectNone = QtGui.QPushButton(Dialog)
        self.btnSelectNone.setObjectName(_fromUtf8("btnSelectNone"))
        self.horizontalLayout_2.addWidget(self.btnSelectNone)
        self.btnClearList = QtGui.QPushButton(Dialog)
        self.btnClearList.setObjectName(_fromUtf8("btnClearList"))
        self.horizontalLayout_2.addWidget(self.btnClearList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Build spatial index", None))
        self.chkExternalFiles.setText(_translate("Dialog", "Select files from disk", None))
        self.btnSelectFiles.setText(_translate("Dialog", "Select files...", None))
        self.btnSelectAll.setText(_translate("Dialog", "Select all", None))
        self.btnSelectNone.setText(_translate("Dialog", "Select none", None))
        self.btnClearList.setText(_translate("Dialog", "Clear list", None))

