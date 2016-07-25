# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParcelSearchDialog
                                 A QGIS plugin
 Search by UniqueParcelID
                             -------------------
        begin                : 2016-04-13
        git sha              : $Format:%H$
        copyright            : (C) 2016 by INSA
        email                : robel.g@insa.gov.et
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
from qgis.core import *
from PyQt4 import QtGui, uic
from qgis.utils import *
from PyQt4.QtGui import QMessageBox
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'parcel_search_dialog_base.ui'))


class ParcelSearchDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ParcelSearchDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.cancelButton.clicked.connect(self.cancelButtonClicked)
    def searchButtonClicked(self):
                active_layer = iface.activeLayer()
                self.pId = self.unqParcelIDText.text()
                layers=iface.legendInterface().layers()
                ids = []
                for layer in layers:
                    if layer.name() == 'PARCEL':
                        itr = layer.getFeatures() 
                        self.idd = str(self.pId)
                        for i in itr:
                            if self.idd == str(i['UNIQUEPARCELID']):
                              ids.append(i.id())
                print ids
                active_layer.setSelectedFeatures(ids)
                mCanvas = iface.mapCanvas()
                mCanvas.zoomToSelected()
                
                if not ids:
        
                    QMessageBox.information(self, "Invalid Parcel ID", "Invalid Unique Parcel ID \n Please Enter a Valid Unique Parcel ID!")

    def cancelButtonClicked(self):
         self.close()
