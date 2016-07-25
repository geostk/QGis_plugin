# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmReProject.ui'
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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(377, 476)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.inShape = QtGui.QComboBox(Dialog)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.verticalLayout.addWidget(self.inShape)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.inRef = QtGui.QLineEdit(Dialog)
        self.inRef.setReadOnly(True)
        self.inRef.setObjectName(_fromUtf8("inRef"))
        self.verticalLayout_2.addWidget(self.inRef)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.rdoProjection = QtGui.QRadioButton(self.groupBox)
        self.rdoProjection.setChecked(True)
        self.rdoProjection.setObjectName(_fromUtf8("rdoProjection"))
        self.gridlayout.addWidget(self.rdoProjection, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.txtProjection = QtGui.QLineEdit(self.groupBox)
        self.txtProjection.setReadOnly(True)
        self.txtProjection.setObjectName(_fromUtf8("txtProjection"))
        self.hboxlayout.addWidget(self.txtProjection)
        self.btnProjection = QtGui.QPushButton(self.groupBox)
        self.btnProjection.setObjectName(_fromUtf8("btnProjection"))
        self.hboxlayout.addWidget(self.btnProjection)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridlayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.cmbLayer = QtGui.QComboBox(self.groupBox)
        self.cmbLayer.setEnabled(False)
        self.cmbLayer.setObjectName(_fromUtf8("cmbLayer"))
        self.gridlayout.addWidget(self.cmbLayer, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.outRef = QtGui.QLineEdit(self.groupBox)
        self.outRef.setEnabled(False)
        self.outRef.setReadOnly(True)
        self.outRef.setObjectName(_fromUtf8("outRef"))
        self.gridlayout.addWidget(self.outRef, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.hboxlayout1.addWidget(self.outShape)
        self.toolOut = QtGui.QPushButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.hboxlayout1.addWidget(self.toolOut)
        self.verticalLayout_3.addLayout(self.hboxlayout1)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QObject.connect(self.rdoProjection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txtProjection.setEnabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cmbLayer.setEnabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_5.setEnabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.outRef.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Projection Management Tool", None))
        self.label_3.setText(_translate("Dialog", "Input vector layer", None))
        self.label_4.setText(_translate("Dialog", "Input spatial reference system", None))
        self.groupBox.setTitle(_translate("Dialog", "Output spatial reference system", None))
        self.rdoProjection.setText(_translate("Dialog", "Use predefined spatial reference system", None))
        self.btnProjection.setText(_translate("Dialog", "Choose", None))
        self.radioButton_2.setText(_translate("Dialog", "Import spatial reference system from existing layer", None))
        self.label_5.setText(_translate("Dialog", "Import spatial reference system", None))
        self.label_2.setText(_translate("Dialog", "Output Shapefile", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))

