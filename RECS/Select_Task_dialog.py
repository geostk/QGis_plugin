# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectTaskDialog
                                 A QGIS plugin
 This Plugin displays a list of Tasks.
                             -------------------
        begin                : 2015-07-07
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
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QMessageBox, QAction,QTableWidget
from PyQt4 import QtGui, uic
from PyQt4 import QtCore
import sys
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from gmlToShape import GmlToShape
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/Select_Task_dialog_base.ui'))


class SelectTaskDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTaskDialog, self).__init__(parent)

        self.setupUi(self)
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)
        self.canvas.resize(QtCore.QSize(200, 200))
        self.canvas.useImageToRender(True)
        layout = QtGui.QGridLayout(self.frame)
        layout.addWidget(self.canvas)
        self.taskListTable.cellClicked.connect(self.rowClicked)
        #self.taskListTable.doubleClicked.connect(self.xx)
        self.selectTaskButton.clicked.connect(self.loadTaskClicked)
        self.noTaskButton.clicked.connect(self.noTaskClicked)
        self.taskListTable.setSelectionBehavior(QTableWidget.SelectRows)
        # self.taskListTable.setSelectionBehavior(SelectRows())
        self.quitButton.clicked.connect(self.quitClicked)
        header = self.taskListTable.horizontalHeader()
        header.setStretchLastSection(True)
        header2 = self.propertiesTable.horizontalHeader()
        header2.setStretchLastSection(True)
        self.taskListTable.verticalHeader().setVisible(False)
        self.propertiesTable.horizontalHeader().setVisible(False)
    def populate(self):


        # import psycopg2
        import cx_Oracle
        global columnValue

        try:
            connstr = ('common/common@172.20.0.71:1521/sccdb')
            # conn = psycopg2.connect("dbname='ncrprs_db' user='postgres' host='172.20.0.71' password='123456'")
            # cur = conn.cursor()
            conn=cx_Oracle.connect(connstr)
            cur=conn.cursor()
            #cur.execute("select * from V_L1_Task where System like '%s' order by CreationDate desc"%('RECS'))
          
            cur.execute(
                "SELECT  taskid, createdby, modifiedby, creationdate, modificationdate,  TRANSACTIONTYPEIDFK FROM common.t_task where system like '%s' order by taskid desc"%('RECS'))
            rows = cur.fetchall()

            xrows = len(rows)
            xcolumn = len(rows[0])
            i = 1
            j = 0
            self.taskListTable.setSortingEnabled(True)
            self.taskListTable.setColumnCount(xcolumn)
            self.taskListTable.setRowCount(xrows)
            self.taskListTable.setHorizontalHeaderLabels(
                ['TaskID', 'Created By', 'Modified By', 'Creation Date', 'Modification Date', 'Task Status'])
            for i in range(xrows):
                for j in range(xcolumn):
                    item = QtGui.QTableWidgetItem(str(rows[i][j]))
                    self.taskListTable.setItem(i, j, item)
                    item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                    #
                    # self.taskListTable.item(xrows,2).setFlags(QtCore.Qt.IsSelectable)

        except:
            QMessageBox.information(self, "Connection Error", "Can't connect to DataBase!")
            

    def loadLayer(self):


        #QgsMapLayerRegistry.instance().removeAllMapLayers()
        self.mlr = QgsMapLayerRegistry.instance()
        uri = QgsDataSourceURI()
        uri.setConnection("172.20.0.71", "5432", "ncrprs_db", "postgres", "123456")
        uri.setDataSource("recs", "t_parcel", "parcelgeometry", "")
        vlayer = QgsVectorLayer(uri.uri(), "Parcel", "postgres")
        if vlayer.isValid():
            self.mlr.addMapLayer(vlayer)
            cl = QgsMapCanvasLayer(vlayer)
            layers = [cl]

            self.canvas.setExtent(vlayer.extent())
            self.canvas.setLayerSet(layers)
        else:
            QMessageBox.information(self, "Unable to Connect to Database", "Unable to Load Layers from the Database!")


    def rowClicked(self):

        global taskID
        indexes = self.taskListTable.selectionModel().selectedRows()
        for index in sorted(indexes):

                row=index.row()
                itm = self.taskListTable.item(row, 0)
                taskID = itm.text()

        import cx_Oracle


        try:
            connstr = ('common/common@172.20.0.71:1521/sccdb')
            conn=cx_Oracle.connect(connstr)



            # conn = psycopg2.connect("dbname='ncrprs_db' user='postgres' host='172.20.0.71' password='123456'")
            cur = conn.cursor()

            cur.execute(
                "SELECT  taskid, createdby, modifiedby, creationdate, modificationdate, beginlifespan, endlifespan, comments FROM common.t_task WHERE taskid = '%s'" % (
                    taskID))
            rows = cur.fetchall()
            xrows = len(rows)
            xcolumn = len(rows[0])

            self.propertiesTable.setColumnCount(xrows)
            self.propertiesTable.setRowCount(xcolumn)
            self.propertiesTable.setVerticalHeaderLabels(
                ['TaskID', 'Created By', 'Modified By', 'Creation Date', 'Modification Date', 'Begin Life Span',
                 'End Life Span', 'Task Status', 'Comment'])
            for column in range(xcolumn):
                for row in range(xrows):
                    item = QtGui.QTableWidgetItem(str(rows[row][column]))
                    self.propertiesTable.setItem(row, column, item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)


        except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect to Server!")




        
    def gmlWrite(self):
        import os
        from suds.client import Client





        try:
            indexes = self.taskListTable.selectionModel().selectedRows()
            for index in sorted(indexes):
                 row=index.row()
                 # column=item(row,0)
                 itm = self.taskListTable.item(row, 0)
                 taskID = itm.text()

            subSystem="RECS"

                 # QMessageBox.information(self, "Layer Error", "Row %s is selected" % (x))



            dirname = "{HOME}/Documents/GMLFile/"

            pathDir = os.path.dirname(dirname)
            if not os.path.exists(pathDir):
              os.makedirs(pathDir)
            url="http://172.20.85.48/wcfService1/Service1.svc?wsdl"
            client=Client(url)
            gml=client.service.LoadTaskData(taskID,subSystem)
            save_path = '{HOME}/Documents/GMLFile/'
            name_of_file = "parcelGML"
            completeName = os.path.join(save_path,name_of_file+".gml")
            openFile = open(completeName, "w")
            # openFile.write(" ".join([" ".join(v) for v in gml]))
            openFile.write(gml)
            openFile.close()
        except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect to Service")
            
    def loadTaskClicked(self):
        import logging
       
        #
        # try:
        #
        #     vlayer_crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
        #     iface.mapCanvas().mapRenderer().setDestinationCrs(vlayer_crs)
        #     iface.addVectorLayer("{HOME}/Documents/GMLFile/parcelGML.gml","gmlToShape","ogr")
        #     _vlayer = iface.activeLayer()
        #
        #     QgsVectorFileWriter.writeAsVectorFormat(_vlayer,"{HOME}/Documents/GMLFile/parcel.shp","utf-8",None,"ESRI Shapefile")
        #     QgsMapLayerRegistry.instance().removeAllMapLayers()
        #     iface.addVectorLayer("{HOME}/Documents/GMLFile/parcel.shp","ParcelWithNeighbour","ogr")
        #     self.close()
        #
        #
        # except:
        #
        #       QMessageBox.information(self, "Error", "Select a Task From the List!")
        import  pickle
        f2 = open('Z:\session','rb')
        user = pickle.load(f2)
        gmlShape=GmlToShape()
        gmlShape.createShape(taskID)
        logging.basicConfig(format='%(asctime)s %(message)s',filename='Z:\Log\AACADIS.RECS.log_%s'%user,level=logging.INFO)
        logging.info('Task Loaded successfully from Select Task Grid - TaskID:%s'%taskID)
        self.close()
    def noTaskClicked(self):
        global taskID
        taskID = None
        self.close()
        #self.loadLayer()
    def quitClicked(self):
         sys.exit(self)

    def retTaskID(self):
        return  taskID


   







