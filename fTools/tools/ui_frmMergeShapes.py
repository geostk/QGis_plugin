# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmMergeShapes.ui'
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
        Dialog.resize(377, 302)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chkListMode = QtGui.QCheckBox(Dialog)
        self.chkListMode.setObjectName(_fromUtf8("chkListMode"))
        self.verticalLayout.addWidget(self.chkListMode)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblGeometry = QtGui.QLabel(Dialog)
        self.lblGeometry.setObjectName(_fromUtf8("lblGeometry"))
        self.horizontalLayout_3.addWidget(self.lblGeometry)
        self.cmbGeometry = QtGui.QComboBox(Dialog)
        self.cmbGeometry.setObjectName(_fromUtf8("cmbGeometry"))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbGeometry)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leInputDir = QtGui.QLineEdit(Dialog)
        self.leInputDir.setObjectName(_fromUtf8("leInputDir"))
        self.horizontalLayout.addWidget(self.leInputDir)
        self.btnSelectDir = QtGui.QPushButton(Dialog)
        self.btnSelectDir.setObjectName(_fromUtf8("btnSelectDir"))
        self.horizontalLayout.addWidget(self.btnSelectDir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.leOutShape = QtGui.QLineEdit(Dialog)
        self.leOutShape.setObjectName(_fromUtf8("leOutShape"))
        self.horizontalLayout_2.addWidget(self.leOutShape)
        self.btnSelectFile = QtGui.QPushButton(Dialog)
        self.btnSelectFile.setObjectName(_fromUtf8("btnSelectFile"))
        self.horizontalLayout_2.addWidget(self.btnSelectFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chkAddToCanvas = QtGui.QCheckBox(Dialog)
        self.chkAddToCanvas.setChecked(True)
        self.chkAddToCanvas.setObjectName(_fromUtf8("chkAddToCanvas"))
        self.verticalLayout.addWidget(self.chkAddToCanvas)
        self.progressFeatures = QtGui.QProgressBar(Dialog)
        self.progressFeatures.setProperty("value", 0)
        self.progressFeatures.setObjectName(_fromUtf8("progressFeatures"))
        self.verticalLayout.addWidget(self.progressFeatures)
        self.progressFiles = QtGui.QProgressBar(Dialog)
        self.progressFiles.setProperty("value", 0)
        self.progressFiles.setObjectName(_fromUtf8("progressFiles"))
        self.verticalLayout.addWidget(self.progressFiles)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Merge shapefiles", None))
        self.chkListMode.setText(_translate("Dialog", "Select by layers in the folder", None))
        self.lblGeometry.setText(_translate("Dialog", "Shapefile type", None))
        self.cmbGeometry.setItemText(0, _translate("Dialog", "Polygon", None))
        self.cmbGeometry.setItemText(1, _translate("Dialog", "Line", None))
        self.cmbGeometry.setItemText(2, _translate("Dialog", "Point", None))
        self.label.setText(_translate("Dialog", "Input directory", None))
        self.btnSelectDir.setText(_translate("Dialog", "Browse", None))
        self.label_2.setText(_translate("Dialog", "Output shapefile", None))
        self.btnSelectFile.setText(_translate("Dialog", "Browse", None))
        self.chkAddToCanvas.setText(_translate("Dialog", "Add result to map canvas", None))

