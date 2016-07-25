# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmSimplify.ui'
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
        Dialog.resize(400, 269)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.cmbInputLayer = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbInputLayer.sizePolicy().hasHeightForWidth())
        self.cmbInputLayer.setSizePolicy(sizePolicy)
        self.cmbInputLayer.setObjectName(_fromUtf8("cmbInputLayer"))
        self.verticalLayout.addWidget(self.cmbInputLayer)
        self.chkUseSelection = QtGui.QCheckBox(Dialog)
        self.chkUseSelection.setObjectName(_fromUtf8("chkUseSelection"))
        self.verticalLayout.addWidget(self.chkUseSelection)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblTolerance = QtGui.QLabel(Dialog)
        self.lblTolerance.setObjectName(_fromUtf8("lblTolerance"))
        self.horizontalLayout_3.addWidget(self.lblTolerance)
        self.spnTolerance = QtGui.QDoubleSpinBox(Dialog)
        self.spnTolerance.setDecimals(4)
        self.spnTolerance.setMinimum(0.0)
        self.spnTolerance.setMaximum(10000000.0)
        self.spnTolerance.setProperty("value", 0.0001)
        self.spnTolerance.setObjectName(_fromUtf8("spnTolerance"))
        self.horizontalLayout_3.addWidget(self.spnTolerance)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chkWriteShapefile = QtGui.QCheckBox(Dialog)
        self.chkWriteShapefile.setObjectName(_fromUtf8("chkWriteShapefile"))
        self.horizontalLayout_2.addWidget(self.chkWriteShapefile)
        self.edOutputFile = QtGui.QLineEdit(Dialog)
        self.edOutputFile.setEnabled(False)
        self.edOutputFile.setObjectName(_fromUtf8("edOutputFile"))
        self.horizontalLayout_2.addWidget(self.edOutputFile)
        self.btnSelectOutputFile = QtGui.QPushButton(Dialog)
        self.btnSelectOutputFile.setEnabled(False)
        self.btnSelectOutputFile.setObjectName(_fromUtf8("btnSelectOutputFile"))
        self.horizontalLayout_2.addWidget(self.btnSelectOutputFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chkAddToCanvas = QtGui.QCheckBox(Dialog)
        self.chkAddToCanvas.setEnabled(False)
        self.chkAddToCanvas.setChecked(True)
        self.chkAddToCanvas.setObjectName(_fromUtf8("chkAddToCanvas"))
        self.verticalLayout.addWidget(self.chkAddToCanvas)
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
        Dialog.setWindowTitle(_translate("Dialog", "Simplify geometries", None))
        self.label.setText(_translate("Dialog", "Input line or polygon layer", None))
        self.chkUseSelection.setText(_translate("Dialog", "Use only selected features", None))
        self.lblTolerance.setText(_translate("Dialog", "Simplify tolerance", None))
        self.chkWriteShapefile.setText(_translate("Dialog", "Save to new file", None))
        self.btnSelectOutputFile.setText(_translate("Dialog", "Browse", None))
        self.chkAddToCanvas.setText(_translate("Dialog", "Add result to canvas", None))

