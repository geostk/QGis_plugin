__author__ = 'Robel'
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FeatureCurrentTaskDialog
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
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QMessageBox, QAction,QTableWidget
from PyQt4 import QtGui, uic
from PyQt4 import QtCore
import sys
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from Connection import ConnectionHandler
from task_oid import FeatureTask
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/features_of_current_task.ui'))


class taskFeatures(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(taskFeatures, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.currentTaskTable.cellClicked.connect(self.rowClicked)
        self.currentTaskTable.verticalHeader().setVisible(False)
        header = self.currentTaskTable.horizontalHeader()
        header.setStretchLastSection(True)
        self.currentTaskTable.setSelectionBehavior(QTableWidget.SelectRows)

    def populate(self,taskID):
        featuresOfTask=FeatureTask()
        lst_oid=featuresOfTask.taskOid(taskID)
        i = 1
        j = 0
        no_rows = len(lst_oid)
        no_column=15
        x= ', '.join(lst_oid)
        #z='"'+'", "'.join(lst_oid)+'"'
        oids="'"+"', '".join(lst_oid)+"'"
        self.currentTaskTable.setColumnCount(no_column)
        self.currentTaskTable.setRowCount(no_rows)
        self.currentTaskTable.setHorizontalHeaderLabels(['Unique Parcel ID','Block No', 'Street Name', 'Street No', 'Woreda Code', ' Area', 'Area_D','Area_M','Perimeter','Perimeter_D','Perimeter_M','OID','Begin Lifespan','End Lifespan','Voided','Surveyed'])

        con=ConnectionHandler()
        cur=con.connect_RECS()
        cur.execute( "select uniqueparcelid,block_no,street_name,street_no,woredacode, area,area_d,area_m,perimeter,perimeter_d,perimeter_m,oid,beginlifespan,endlifespan,voided,surveyed from v_l2_parcel where oid in (%s)" % (oids))

        fetchedData=cur.fetchall()
        print fetchedData
        for i in range(no_rows):
            for j in range(no_column):
                item = QtGui.QTableWidgetItem(str(fetchedData[i][j]))
                self.currentTaskTable.setItem(i, j, item)
                item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)


    def rowClicked(self):
		lst_task=[]
		indexes = self.currentTaskTable.selectionModel().selectedRows()
		lst_items=[]
		for index in sorted(indexes):
			row=index.row()
			uniqueParcl = self.currentTaskTable.item(row, 0)
			lst_task.append(uniqueParcl.text())
			block_no=self.currentTaskTable.item(row, 1).text()
			lst_task.append(block_no)
			str_name=self.currentTaskTable.item(row, 2).text()
			lst_task.append(str_name)
			strt_no=self.currentTaskTable.item(row, 3).text()
			lst_task.append(strt_no)
			woredacode=self.currentTaskTable.item(row, 4).text()
			lst_task.append(woredacode)
			area=self.currentTaskTable.item(row, 5).text()
			lst_task.append(area)
			area_d=self.currentTaskTable.item(row,6).text()
			lst_task.append(area_d)
			area_m=self.currentTaskTable.item(row,7).text()
			lst_task.append(area_m)
			perimeter=self.currentTaskTable.item(row,8).text()
			lst_task.append(perimeter)
			perimeter_d=self.currentTaskTable.item(row,9).text()
			lst_task.append(perimeter_d)
			perimeter_m=self.currentTaskTable.item(row,10).text()
			lst_task.append(perimeter_m)
			oid=self.currentTaskTable.item(row,11).text()
			lst_task.append(oid)
			beginlifespan=self.currentTaskTable.item(row,12).text()
			lst_task.append(beginlifespan)
			endlifespan=self.currentTaskTable.item(row,13).text()
			lst_task.append(endlifespan)
		print lst_task
		return lst_task
				
				
				
				
				
				
				


