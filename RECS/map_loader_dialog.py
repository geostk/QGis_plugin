# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadMapDialog
                                 A QGIS plugin
 loads map from database
                             -------------------
        begin                : 2015-02-26
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Mael
        email                : mael.taye@insa.gov.et
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog

import os.path
import time
import thread
import time
from qgis.gui import  *
from qgis.core import *

from PyQt4 import QtGui, uic

#FORM_CLASS, _ = uic.loadUiType(os.path.join(
 #   os.path.dirname(__file__), 'map_loader_dialog_base.ui'))


class LoadMapDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LoadMapDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.loadLayer()
    def loadLayer(self):
        self.mlr = None
        # QgsMapLayerRegistry.instance().removeAllMapLayers()
        self.mlr = QgsMapLayerRegistry.instance()
        uri = QgsDataSourceURI()
        uri.setConnection("172.20.0.71", "5432", "ncrprs_db", "postgres", "123456")
        uri.setDataSource("recs", "t_parcel", "parcelgeometry", "")
        vlayer = QgsVectorLayer(uri.uri(), "Parcel", "postgres")
        if vlayer.isValid():
            self.mlr.addMapLayer(vlayer)
        else:
            QMessageBox.information(None, "Unable to Laod Data", "Unable to Load Layers from the Database!")
            return None
            # def temp(self,e):

