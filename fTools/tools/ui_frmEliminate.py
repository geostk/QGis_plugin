# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmEliminate.ui'
#
# Created: Wed Jul 29 01:08:21 2015
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
        Dialog.resize(436, 242)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.boundary = QtGui.QRadioButton(Dialog)
        self.boundary.setObjectName(_fromUtf8("boundary"))
        self.gridLayout.addWidget(self.boundary, 4, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.horizontalLayout.addWidget(self.outShape)
        self.toolOut = QtGui.QPushButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.horizontalLayout.addWidget(self.toolOut)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.gridLayout.addWidget(self.buttonBox_2, 7, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.inShape = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inShape.sizePolicy().hasHeightForWidth())
        self.inShape.setSizePolicy(sizePolicy)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.horizontalLayout_2.addWidget(self.inShape)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
        self.addToCanvasCheck.setChecked(True)
        self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
        self.gridLayout.addWidget(self.addToCanvasCheck, 6, 0, 1, 1)
        self.selected = QtGui.QLabel(Dialog)
        self.selected.setObjectName(_fromUtf8("selected"))
        self.gridLayout.addWidget(self.selected, 1, 0, 1, 1)
        self.area = QtGui.QRadioButton(Dialog)
        self.area.setObjectName(_fromUtf8("area"))
        self.gridLayout.addWidget(self.area, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Eliminate sliver polygons", None))
        self.boundary.setText(_translate("Dialog", "common boundary", None))
        self.label.setText(_translate("Dialog", "Merge selection with the neighbouring polygon with the largest", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))
        self.label_3.setText(_translate("Dialog", "Input vector layer", None))
        self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))
        self.selected.setText(_translate("Dialog", "Selected features:", None))
        self.area.setText(_translate("Dialog", "area", None))

