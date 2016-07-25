# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetClipper.ui'
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
        GdalToolsWidget.resize(338, 226)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.noDataCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.noDataCheck.setObjectName(_fromUtf8("noDataCheck"))
        self.gridLayout.addWidget(self.noDataCheck, 2, 0, 1, 1)
        self.noDataSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.noDataSpin.setMinimum(-100000)
        self.noDataSpin.setMaximum(65000)
        self.noDataSpin.setObjectName(_fromUtf8("noDataSpin"))
        self.gridLayout.addWidget(self.noDataSpin, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(GdalToolsWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.extentGroup = QtGui.QGroupBox(GdalToolsWidget)
        self.extentGroup.setObjectName(_fromUtf8("extentGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.extentGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.extentModeRadio = QtGui.QRadioButton(self.extentGroup)
        self.extentModeRadio.setChecked(True)
        self.extentModeRadio.setObjectName(_fromUtf8("extentModeRadio"))
        self.gridLayout_2.addWidget(self.extentModeRadio, 0, 0, 1, 1)
        self.maskModeRadio = QtGui.QRadioButton(self.extentGroup)
        self.maskModeRadio.setObjectName(_fromUtf8("maskModeRadio"))
        self.gridLayout_2.addWidget(self.maskModeRadio, 0, 1, 1, 1)
        self.modeStackedWidget = QtGui.QStackedWidget(self.extentGroup)
        self.modeStackedWidget.setObjectName(_fromUtf8("modeStackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.extentSelector = GdalToolsExtentSelector(self.page)
        self.extentSelector.setObjectName(_fromUtf8("extentSelector"))
        self.gridLayout_3.addWidget(self.extentSelector, 0, 0, 1, 1)
        self.modeStackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.page_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.maskSelector = GdalToolsInOutSelector(self.page_2)
        self.maskSelector.setObjectName(_fromUtf8("maskSelector"))
        self.gridLayout_4.addWidget(self.maskSelector, 0, 1, 1, 1)
        self.alphaBandCheck = QtGui.QCheckBox(self.page_2)
        self.alphaBandCheck.setObjectName(_fromUtf8("alphaBandCheck"))
        self.gridLayout_4.addWidget(self.alphaBandCheck, 1, 0, 1, 1)
        self.modeStackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.modeStackedWidget, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.extentGroup)
        self.label_2.setBuddy(self.outSelector)
        self.label_3.setBuddy(self.inSelector)

        self.retranslateUi(GdalToolsWidget)
        self.modeStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Clipper", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.noDataCheck.setText(_translate("GdalToolsWidget", "&No data value", None))
        self.label_3.setText(_translate("GdalToolsWidget", "&Input file (raster)", None))
        self.extentGroup.setTitle(_translate("GdalToolsWidget", "Clipping mode", None))
        self.extentModeRadio.setText(_translate("GdalToolsWidget", "Extent", None))
        self.maskModeRadio.setText(_translate("GdalToolsWidget", "Mask layer", None))
        self.label.setText(_translate("GdalToolsWidget", "Mask layer", None))
        self.alphaBandCheck.setText(_translate("GdalToolsWidget", "Create an output alpha band", None))

from extentSelector import GdalToolsExtentSelector
from inOutSelector import GdalToolsInOutSelector
