# -*- coding: utf-8 -*-
"""
***************************************************************************
   QGIS Web Processing Service Plugin
  -------------------------------------------------------------------
 Date                 : 28 April 2015
 Copyright            : (C) 2015 by Gérald Fenoy
 email                : gerald dot fenoy at geoalbs dot fr

  ***************************************************************************
  *                                                                         *
  *   This program is free software; you can redistribute it and/or modify  *
  *   it under the terms of the GNU General Public License as published by  *
  *   the Free Software Foundation; either version 2 of the License, or     *
  *   (at your option) any later version.                                   *
  *                                                                         *
  ***************************************************************************
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from QgsWPSClient import version
from Ui_qgswpstablegui import Ui_QgsWpsTableGUI
import os, sys, string

class QgsWpsTableGui(QDialog, QObject, Ui_QgsWpsTableGUI):
  MSG_BOX_TITLE = "QGIS WPS Client"
  
  def __init__(self, parent, fl, layer):
    QDialog.__init__(self, parent, fl)
    self.setupUi(self)
    self.setWindowTitle('QgsWPSClient-'+version()+' '+layer)
    self.selectedServiceName = parent.cmbConnections.currentText()
    
    
  def currentServiceName(self):
      return self.selectedServiceName 
