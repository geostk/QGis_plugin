# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmSubsetSelect.ui'
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
        Dialog.resize(355, 285)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout.addWidget(self.label_3)
        self.inShape = QtGui.QComboBox(Dialog)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.vboxlayout.addWidget(self.inShape)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 2)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vboxlayout1.addWidget(self.label_4)
        self.inField = QtGui.QComboBox(Dialog)
        self.inField.setObjectName(_fromUtf8("inField"))
        self.vboxlayout1.addWidget(self.inField)
        self.gridLayout.addLayout(self.vboxlayout1, 1, 0, 1, 2)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout3.addWidget(self.label_2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.rdoNumber = QtGui.QRadioButton(Dialog)
        self.rdoNumber.setChecked(True)
        self.rdoNumber.setObjectName(_fromUtf8("rdoNumber"))
        self.hboxlayout.addWidget(self.rdoNumber)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.spnNumber = QtGui.QSpinBox(Dialog)
        self.spnNumber.setMinimum(1)
        self.spnNumber.setObjectName(_fromUtf8("spnNumber"))
        self.hboxlayout.addWidget(self.spnNumber)
        self.vboxlayout3.addLayout(self.hboxlayout)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.rdoPercent = QtGui.QRadioButton(Dialog)
        self.rdoPercent.setObjectName(_fromUtf8("rdoPercent"))
        self.hboxlayout1.addWidget(self.rdoPercent)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.spnPercent = QtGui.QSpinBox(Dialog)
        self.spnPercent.setPrefix(_fromUtf8(""))
        self.spnPercent.setMinimum(1)
        self.spnPercent.setMaximum(100)
        self.spnPercent.setProperty("value", 50)
        self.spnPercent.setObjectName(_fromUtf8("spnPercent"))
        self.hboxlayout1.addWidget(self.spnPercent)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.gridLayout.addLayout(self.vboxlayout2, 2, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.gridLayout.addWidget(self.buttonBox_2, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Random Selection From Within Subsets", None))
        self.label_3.setText(_translate("Dialog", "Input Vector Layer", None))
        self.label_4.setText(_translate("Dialog", "Input subset field (unique ID field)", None))
        self.label_2.setText(_translate("Dialog", "Randomly Select", None))
        self.rdoNumber.setText(_translate("Dialog", "Number of Features", None))
        self.rdoPercent.setText(_translate("Dialog", "Percentage of Features", None))
        self.spnPercent.setSuffix(_translate("Dialog", "%", None))

