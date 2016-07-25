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
from Connection import ConnectionHandler
from UpdateTemplate import FinishTask
from editAttributes import EditAttributes

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/feature_property_dialog.ui'))


class taskInfo(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(taskInfo, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.okButton.clicked.connect(self.updateAttrib)
        self.cancelButton.clicked.connect(self.closeDialog)
    def getAttribData(self,taskID):
		from feature_curent_task_dialog import taskFeatures
		obj=taskFeatures()
		print obj.rowClicked()
		global fetchedData
		global t_id
		t_id = taskID
		obj = FinishTask()
		oid = obj.getOldOid(t_id)
		con=ConnectionHandler()
		cur=con.connect_RECS()
		cur.execute( "select block_no,street_name,street_no,woredacode, area,area_d,area_m,perimeter,perimeter_d,perimeter_m,beginlifespan,endlifespan,voided,surveyed,uniqueparcelid  from v_l2_parcel where oid='%s'"%(oid[0]))
		fetchedData=cur.fetchall()
		print len(fetchedData[0])
		print fetchedData
		self.lineEdit.setText(str(fetchedData[0][14]))
		self.lineEdit_3.setText(str(fetchedData[0][0]))
		self.lineEdit_4.setText(str(fetchedData[0][1]))
		self.lineEdit_5.setText(str(fetchedData[0][2]))
		self.lineEdit_6.setText(str(fetchedData[0][3]))
		self.lineEdit_7.setText(str(fetchedData[0][4]))
		self.lineEdit_8.setText(str(fetchedData[0][5]))
		self.lineEdit_9.setText(str(fetchedData[0][6]))
		self.lineEdit_10.setText(str(fetchedData[0][7]))
		self.lineEdit_14.setText(str(fetchedData[0][10]))
		self.lineEdit_13.setText(oid[0])
		self.lineEdit_15.setText(str(fetchedData[0][11]))

    def updateAttrib(self):
        parcelType = self.comboBox.currentText()
        streetName = self.lineEdit_4.text()
        area_d = self.lineEdit_8.text()
        area_m = self.lineEdit_9.text()
        perimeter_d = self.lineEdit_11.text()
        perimeter_m = self.lineEdit_12.text()
        obj = EditAttributes()
        print "Edit Called"
        obj.ProcessEdit(t_id,parcelType,streetName,area_d,area_m,perimeter_d,perimeter_m)
        QMessageBox.information(self,"Information","Successfully Finished Task!")
        self.close()


    
    def populate(self):
        try:

                system="RECS"
                connect =  ConnectionHandler()
                cur = connect.connect_Common()
                cur.execute("select taskid, transactiontype,createdby,beginlifespan,endlifespan,status,comments from v_l1_task where system like '%s' and taskid like '%s' "%(system,taskId))
                rows = cur.fetchall()
                print rows
                xrows = len(rows)
                print xrows
                xcolumn = len(rows[0])

                model = QtGui.QStandardItemModel(xrows, xcolumn)
                model.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Comment'])
                for i in range(xrows):
                    for j in range(xcolumn):
                        item = QtGui.QStandardItem(str(rows[i][j]))
                        model.setItem(i, j, item)
                        item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                self.taskInfoTable.setModel(model)

        except:
            QMessageBox.information(self, "Message", "No Result Found!")
    def closeDialog(self):
        self.close()