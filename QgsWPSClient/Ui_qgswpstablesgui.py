# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QgsWpsTablesGUI(object):
    def setupUi(self, QgsWpsTablesGUI):
        QgsWpsTablesGUI.setObjectName(_fromUtf8("QgsWpsTablesGUI"))
        QgsWpsTablesGUI.setWindowModality(QtCore.Qt.NonModal)
        QgsWpsTablesGUI.resize(350, 600)
        QgsWpsTablesGUI.setWindowTitle(QtGui.QApplication.translate("QgsWpsTablesGUI", "Display table result", None, QtGui.QApplication.UnicodeUTF8))

        self.retranslateUi(QgsWpsTablesGUI)
        QtCore.QMetaObject.connectSlotsByName(QgsWpsTablesGUI)

    def retranslateUi(self, QgsWpsTablesGUI):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QgsWpsTablesGUI = QtGui.QDialog()
    ui = Ui_QgsWpsTablesGUI()
    ui.setupUi(QgsWpsTablesGUI)
    QgsWpsTablesGUI.show()
    sys.exit(app.exec_())

