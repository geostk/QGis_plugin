# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetBuildVRT.ui'
#
# Created: Wed Jul 29 01:08:12 2015
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

class Ui_GdalToolsWidget(object):
    def setupUi(self, GdalToolsWidget):
        GdalToolsWidget.setObjectName(_fromUtf8("GdalToolsWidget"))
        GdalToolsWidget.resize(348, 266)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inputSelLayersCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.inputSelLayersCheck.setObjectName(_fromUtf8("inputSelLayersCheck"))
        self.gridLayout.addWidget(self.inputSelLayersCheck, 0, 0, 1, 2)
        self.inputDirCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.inputDirCheck.setObjectName(_fromUtf8("inputDirCheck"))
        self.gridLayout.addWidget(self.inputDirCheck, 1, 0, 1, 2)
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.recurseCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.recurseCheck.setObjectName(_fromUtf8("recurseCheck"))
        self.gridLayout.addWidget(self.recurseCheck, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.resolutionCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.resolutionCheck.setObjectName(_fromUtf8("resolutionCheck"))
        self.gridLayout.addWidget(self.resolutionCheck, 5, 0, 1, 1)
        self.resolutionComboBox = QtGui.QComboBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolutionComboBox.sizePolicy().hasHeightForWidth())
        self.resolutionComboBox.setSizePolicy(sizePolicy)
        self.resolutionComboBox.setObjectName(_fromUtf8("resolutionComboBox"))
        self.resolutionComboBox.addItem(_fromUtf8(""))
        self.resolutionComboBox.addItem(_fromUtf8(""))
        self.resolutionComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.resolutionComboBox, 5, 1, 1, 1)
        self.srcNoDataCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.srcNoDataCheck.setObjectName(_fromUtf8("srcNoDataCheck"))
        self.gridLayout.addWidget(self.srcNoDataCheck, 6, 0, 1, 1)
        self.srcNoDataSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.srcNoDataSpin.setMinimum(-100000)
        self.srcNoDataSpin.setMaximum(65000)
        self.srcNoDataSpin.setObjectName(_fromUtf8("srcNoDataSpin"))
        self.gridLayout.addWidget(self.srcNoDataSpin, 6, 1, 1, 1)
        self.separateCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.separateCheck.setObjectName(_fromUtf8("separateCheck"))
        self.gridLayout.addWidget(self.separateCheck, 7, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 2, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 4, 1, 1, 1)
        self.allowProjDiffCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.allowProjDiffCheck.setObjectName(_fromUtf8("allowProjDiffCheck"))
        self.gridLayout.addWidget(self.allowProjDiffCheck, 8, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        self.resolutionComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Build Virtual Raster (Catalog)", None))
        self.inputSelLayersCheck.setText(_translate("GdalToolsWidget", "Use visible raster layers for input", None))
        self.inputDirCheck.setText(_translate("GdalToolsWidget", "Choose input directory instead of files", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input files", None))
        self.recurseCheck.setText(_translate("GdalToolsWidget", "Recurse subdirectories", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.resolutionCheck.setText(_translate("GdalToolsWidget", "&Resolution", None))
        self.resolutionComboBox.setItemText(0, _translate("GdalToolsWidget", "Highest", None))
        self.resolutionComboBox.setItemText(1, _translate("GdalToolsWidget", "Average", None))
        self.resolutionComboBox.setItemText(2, _translate("GdalToolsWidget", "Lowest", None))
        self.srcNoDataCheck.setText(_translate("GdalToolsWidget", "&Source No Data", None))
        self.separateCheck.setText(_translate("GdalToolsWidget", "Se&parate", None))
        self.allowProjDiffCheck.setText(_translate("GdalToolsWidget", "Allow projection difference", None))

from inOutSelector import GdalToolsInOutSelector
