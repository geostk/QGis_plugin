# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TaskDialog
                                 A QGIS plugin
 this tool manage feature tasks
                             -------------------
        begin                : 2015-06-18
        git sha              : $Format:%H$
        copyright            : (C) 2015 by INSA
        email                : INSA@YAHOO.COM
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

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox
from InitTask import InitXML
from checkIfLocked import CheckLocking
from Connection import ConnectionHandler
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtSql import *
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/init_task_dialog_base.ui'))


class InitTaskDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InitTaskDialog, self).__init__(parent)


        self.setupUi(self)
        self.srchButton.clicked.connect(self.searchClicked)
        self.rmvButton.clicked.connect(self.removeClicked)
        self.slctButton.clicked.connect(self.selectClicked)
        self.strtButton.clicked.connect(self.startClicked)
        self.cncelButton.clicked.connect(self.cancelClicked)

        # self.rmvButton.setEnabled(False)
        # self.srchButton.setEnabled(False)

    def searchClicked(self):

      try:


         UPID = self.fetrID.text()
         connect =  ConnectionHandler()
         cur = connect.connect_RECS()
         cur.execute("SELECT ID FROM RECS.T_PARCEL WHERE UNIQUEPARCELID = '%s'" % (UPID))
         ID = cur.fetchall()
         if not ID:
           QMessageBox.information(self, "Message", "Invalid Unique Parcel ID ! \n Please enter a valid unique parcel ID!")
           return None
         active_layer = iface.activeLayer()
         ids = []
         ids.append(ID[0][0])
         print ids
         active_layer.setSelectedFeatures(ids)
         mCanvas = iface.mapCanvas()
         mCanvas.zoomToSelected()
      except:
          QMessageBox.information(self, "Message", "Select a Parcel!")

    def selectClicked(self):
      try:
        self.layer = iface.activeLayer()
        sf = self.layer.selectedFeatures()

        if (self.layer.selectedFeatureCount > 0):
            for f in sf:
                self.temp = str(f['uniqueparcelid'])
                self.featurIDtxt.append(self.temp)

        else:
            QMessageBox.information(self, "Message", "You have no selected feature")
      except:
          QMessageBox.information(self, "Layer Error", "Empty or Invalid Layer!")

    def removeClicked(self):
      try:
        self.fetrID.clear()
        self.featurIDtxt.clear()
        self.cmntText.clear()
      except:
          QMessageBox.information(self, "Error Message", "Empty or Invalid Layer!")

    def startClicked(self):
        import logging
        import pickle
        f2 = open('Z:\session','rb')
        user = pickle.load(f2)
        lock = CheckLocking()
        if lock.isLocked(self.featurIDtxt.toPlainText()) == False:
            inittask = InitXML()
            taskid=inittask.makeintXML(self.featurIDtxt.toPlainText(),self.cmntText.toPlainText())
            QMessageBox.information(self,"Mesage","You have Successfully Initiated a Task! \n TaskID:%s"%(taskid))
            logging.basicConfig(format='%(asctime)s %(message)s',filename='Z:\Log\AACADIS.RECS.log_%s'%user,level=logging.INFO)
            logging.info('Task initiated successfully - unique parcel ID - %s by user %s'%(self.featurIDtxt.toPlainText(),user))
            self.close()
        else:
            QMessageBox.information(self,"Mesage","The Feature you selected is already locked !!!")

    def cancelClicked(self):
        self.close()
