# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmSelectByLocation.ui'
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
        Dialog.resize(534, 321)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 321))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 321))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.inPolygon = QtGui.QComboBox(Dialog)
        self.inPolygon.setObjectName(_fromUtf8("inPolygon"))
        self.verticalLayout_2.addWidget(self.inPolygon)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.inPoint = QtGui.QComboBox(Dialog)
        self.inPoint.setObjectName(_fromUtf8("inPoint"))
        self.verticalLayout_3.addWidget(self.inPoint)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.chkIntersects = QtGui.QCheckBox(Dialog)
        self.chkIntersects.setChecked(True)
        self.chkIntersects.setObjectName(_fromUtf8("chkIntersects"))
        self.verticalLayout.addWidget(self.chkIntersects)
        self.chkTouches = QtGui.QCheckBox(Dialog)
        self.chkTouches.setObjectName(_fromUtf8("chkTouches"))
        self.verticalLayout.addWidget(self.chkTouches)
        self.chkOverlaps = QtGui.QCheckBox(Dialog)
        self.chkOverlaps.setObjectName(_fromUtf8("chkOverlaps"))
        self.verticalLayout.addWidget(self.chkOverlaps)
        self.chkContains = QtGui.QCheckBox(Dialog)
        self.chkContains.setObjectName(_fromUtf8("chkContains"))
        self.verticalLayout.addWidget(self.chkContains)
        self.chkSelected = QtGui.QCheckBox(Dialog)
        self.chkSelected.setObjectName(_fromUtf8("chkSelected"))
        self.verticalLayout.addWidget(self.chkSelected)
        self.cmbModify = QtGui.QComboBox(Dialog)
        self.cmbModify.setObjectName(_fromUtf8("cmbModify"))
        self.verticalLayout.addWidget(self.cmbModify)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.inPolygon, self.inPoint)
        Dialog.setTabOrder(self.inPoint, self.chkIntersects)
        Dialog.setTabOrder(self.chkIntersects, self.chkTouches)
        Dialog.setTabOrder(self.chkTouches, self.chkOverlaps)
        Dialog.setTabOrder(self.chkOverlaps, self.chkContains)
        Dialog.setTabOrder(self.chkContains, self.chkSelected)
        Dialog.setTabOrder(self.chkSelected, self.cmbModify)
        Dialog.setTabOrder(self.cmbModify, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Select by location", None))
        self.label_3.setText(_translate("Dialog", "Select features in:", None))
        self.label_4.setText(_translate("Dialog", "that intersect features in:", None))
        self.chkIntersects.setText(_translate("Dialog", "Include input features that intersect the selection features", None))
        self.chkTouches.setText(_translate("Dialog", "Include input features that touch the selection features", None))
        self.chkOverlaps.setText(_translate("Dialog", "Include input features that overlap/cross the selection features", None))
        self.chkContains.setText(_translate("Dialog", "Include input features completely within the selection features", None))
        self.chkSelected.setText(_translate("Dialog", "Only selected features", None))

