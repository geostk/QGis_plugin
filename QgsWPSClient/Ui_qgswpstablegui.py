# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QgsWpsTableGUI(object):
    def setupUi(self, QgsWpsTableGUI):
        QgsWpsTableGUI.setObjectName(_fromUtf8("QgsWpsTableGUI"))
        QgsWpsTableGUI.setWindowModality(QtCore.Qt.NonModal)
        QgsWpsTableGUI.resize(800, 600)
        QgsWpsTableGUI.setWindowTitle(QtGui.QApplication.translate("QgsWpsTableGUI", "Display table result", None, QtGui.QApplication.UnicodeUTF8))

        self.retranslateUi(QgsWpsTableGUI)
        QtCore.QMetaObject.connectSlotsByName(QgsWpsTableGUI)

    def retranslateUi(self, QgsWpsTableGUI):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QgsWpsTableGUI = QtGui.QDialog()
    ui = Ui_QgsWpsTableGUI()
    ui.setupUi(QgsWpsTableGUI)
    QgsWpsTableGUI.show()
    sys.exit(app.exec_())

