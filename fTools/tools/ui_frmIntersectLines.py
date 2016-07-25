# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmIntersectLines.ui'
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
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(382, 411)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vboxlayout.addWidget(self.label_4)
        self.inLine1 = QtGui.QComboBox(Dialog)
        self.inLine1.setObjectName(_fromUtf8("inLine1"))
        self.vboxlayout.addWidget(self.inLine1)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.vboxlayout1.addWidget(self.label_6)
        self.inField1 = QtGui.QComboBox(Dialog)
        self.inField1.setObjectName(_fromUtf8("inField1"))
        self.vboxlayout1.addWidget(self.inField1)
        self.gridLayout.addLayout(self.vboxlayout1, 1, 0, 1, 1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout2.addWidget(self.label_3)
        self.inLine2 = QtGui.QComboBox(Dialog)
        self.inLine2.setObjectName(_fromUtf8("inLine2"))
        self.vboxlayout2.addWidget(self.inLine2)
        self.gridLayout.addLayout(self.vboxlayout2, 2, 0, 1, 1)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.vboxlayout3.addWidget(self.label_5)
        self.inField2 = QtGui.QComboBox(Dialog)
        self.inField2.setObjectName(_fromUtf8("inField2"))
        self.vboxlayout3.addWidget(self.inField2)
        self.gridLayout.addLayout(self.vboxlayout3, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout4.addWidget(self.label_2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.hboxlayout.addWidget(self.outShape)
        self.toolOut = QtGui.QPushButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.hboxlayout.addWidget(self.toolOut)
        self.vboxlayout4.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.vboxlayout4, 5, 0, 1, 1)
        self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
        self.addToCanvasCheck.setChecked(True)
        self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
        self.gridLayout.addWidget(self.addToCanvasCheck, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.horizontalLayout.addWidget(self.buttonBox_2)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Locate Line Intersections", None))
        self.label_4.setText(_translate("Dialog", "Input line layer", None))
        self.label_6.setText(_translate("Dialog", "Input unique ID field", None))
        self.label_3.setText(_translate("Dialog", "Intersect line layer", None))
        self.label_5.setText(_translate("Dialog", "Intersect unique ID field", None))
        self.label_2.setText(_translate("Dialog", "Output Shapefile", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))
        self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))

