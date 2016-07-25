# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmGeometry.ui'
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
        Dialog.resize(390, 420)
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
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.lineEdit = QtGui.QDoubleSpinBox(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit.setDecimals(4)
        self.lineEdit.setMaximum(100000.0)
        self.lineEdit.setSingleStep(0.5)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.hboxlayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.lblField = QtGui.QLabel(self.splitter)
        self.lblField.setObjectName(_fromUtf8("lblField"))
        self.cmbField = QtGui.QComboBox(self.splitter)
        self.cmbField.setObjectName(_fromUtf8("cmbField"))
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.lblCalcType = QtGui.QLabel(Dialog)
        self.lblCalcType.setObjectName(_fromUtf8("lblCalcType"))
        self._2.addWidget(self.lblCalcType)
        self.cmbCalcType = QtGui.QComboBox(Dialog)
        self.cmbCalcType.setObjectName(_fromUtf8("cmbCalcType"))
        self._2.addWidget(self.cmbCalcType)
        self.gridLayout.addLayout(self._2, 3, 0, 1, 1)
        self.chkUseSelection = QtGui.QCheckBox(Dialog)
        self.chkUseSelection.setObjectName(_fromUtf8("chkUseSelection"))
        self.gridLayout.addWidget(self.chkUseSelection, 4, 0, 1, 1)
        self.chkByFeatures = QtGui.QCheckBox(Dialog)
        self.chkByFeatures.setObjectName(_fromUtf8("chkByFeatures"))
        self.gridLayout.addWidget(self.chkByFeatures, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.chkWriteShapefile = QtGui.QCheckBox(Dialog)
        self.chkWriteShapefile.setObjectName(_fromUtf8("chkWriteShapefile"))
        self.vboxlayout1.addWidget(self.chkWriteShapefile)
        self.lblOutputShapefile = QtGui.QLabel(Dialog)
        self.lblOutputShapefile.setObjectName(_fromUtf8("lblOutputShapefile"))
        self.vboxlayout1.addWidget(self.lblOutputShapefile)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.hboxlayout1.addWidget(self.outShape)
        self.toolOut = QtGui.QPushButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.hboxlayout1.addWidget(self.toolOut)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.gridLayout.addLayout(self.vboxlayout1, 7, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
        self.addToCanvasCheck.setChecked(True)
        self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
        self.gridLayout.addWidget(self.addToCanvasCheck, 9, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 10, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Extract Nodes", None))
        self.label_3.setText(_translate("Dialog", "Input line or polygon vector layer", None))
        self.label.setText(_translate("Dialog", "Tolerance", None))
        self.lblField.setText(_translate("Dialog", "Unique ID field", None))
        self.lblCalcType.setText(_translate("Dialog", "Calculate using", None))
        self.chkUseSelection.setText(_translate("Dialog", "Use only selected features", None))
        self.chkByFeatures.setText(_translate("Dialog", "Calculate extent for each feature separately", None))
        self.chkWriteShapefile.setText(_translate("Dialog", "Save to new shapefile", None))
        self.lblOutputShapefile.setText(_translate("Dialog", "Output point shapefile", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))
        self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))

