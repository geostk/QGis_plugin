# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LogInDialog
                                 A QGIS plugin
 This Plugin is used to authenticate a user
                             -------------------
        begin                : 2015-07-03
        git sha              : $Format:%H$
        copyright            : (C) 2015 by INSA
        email                : robgirma@yahoo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import ldap
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
import logging

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/Log_In_dialog_base.ui'))
attemptCount = 0

class LogInDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LogInDialog, self).__init__(parent)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginClicked)
        self.pushButton_2.clicked.connect(self.cancelClicked)


    def loginClicked(self):
        usr = self.username.text()
        passwd = self.password.text()
        global attemptCount
        logging.basicConfig(format='%(asctime)s %(message)s',filename='Z:\Log\AACADIS.RECS.log_%s'%usr,level=logging.INFO)

        logging.info('Logging In user %s'%usr)
        if usr == "" or passwd == "":
            QMessageBox.information(self, "Empty Field", "Please Fill The Fields Correctly!")
        else:

            try:

                logging.info('Authenticating user %s'%usr)
                l = ldap.open("172.20.0.71")
                l.simple_bind_s(usr, passwd)
                self.accept()
                import pickle
                try:
                    f1 = open('Z:\session','wb')
                    pickle.dump(usr, f1)
                    f1.close()
                    logging.info('Successfully logged in user %s'%usr)
                    iface.mainWindow().statusBar().showMessage(u"Wait Loading a Layer... ")
                except:
                    QMessageBox.information(self, "Message", "Please try to connect to remote drive!")
                    logging.info('Failed to connect to remote drive Z:/')
                    sys.exit(self)

            except ldap.INVALID_CREDENTIALS:
                    #self.validationLabel.setText("Invalid Username or Password")
                    logging.info('Authentication failed for user %s'%usr)
                    QMessageBox.information(self, "Authentication Failed", "Invalid Username or Password\n Please Try Again!")
                    attemptCount +=1
                    if attemptCount == 3:
                        sys.exit(self)

            except ldap.LDAPError, e:
                    QMessageBox.information(self, "Connection Error", "Unable to connect to server!!!\n\n%s" % e)

    def cancelClicked(self):

        self.close()

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message', "Are You Sure to Quit?", QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            sys.exit(self)
        else:
            event.ignore()
