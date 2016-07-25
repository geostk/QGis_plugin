# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TaskManagerDialog
                                 A QGIS plugin
 Mange and Load Tasks
                             -------------------
        begin                : 2015-09-03
        git sha              : $Format:%H$
        copyright            : (C) 2015 by INSA
        email                : robgirmay@yahoo.com
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
from ServiceHandler import ServiceHandler
from Connection import ConnectionHandler
from PyQt4 import QtCore
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox, QAction,QTableWidget
from PyQt4.QtGui import QMessageBox,QDockWidget
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from gmlParse import GMLParser
from ShowTaskArea import showTaskArea
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import SIGNAL
from LoadTask import LoadTask
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/task_manager_dialog_base.ui'))


class TaskManagerDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(TaskManagerDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        taskID=None
        self.taskListTable.clicked.connect(self.rowClicked)
        self.showTaskareaButton.clicked.connect(self.showTaskAreaClicked)
        self.loadfTaskButton.clicked.connect(self.loadTaskClicked(taskID))
        self.refreshTaskButton.clicked.connect(self.populate)
        self.dateTimeEdit.dateChanged.connect(self.dateChanged)
        #self.dateTimeEdit.dateChanged.connect(self.updateByDate)
        #self.connect(self.dateTimeEdit,SIGNAL("dateTimeChanged(QDateEdit)"),self.modifiedDate)
        self.taskListTable.setSelectionBehavior(QTableWidget.SelectRows)
        header = self.taskListTable.horizontalHeader()
        header.setStretchLastSection(True)
        header2 = self.propertiesTable.horizontalHeader()
        header2.setStretchLastSection(True)
        self.taskListTable.verticalHeader().setVisible(False)
        self.propertiesTable.horizontalHeader().setVisible(False)
        self.dateTimeEdit.setCalendarPopup(True)

    def populate(self):

            global model
            system='RECS'
            connect =  ConnectionHandler()
            cur = connect.connect_Common()
            cur.execute("select taskid, createdby,status,beginlifespan,endlifespan,MODIFICATIONDATE,comments from v_l1_task where system like '%s'"%(system))
            rows = cur.fetchall()
            xrows = len(rows)
            xcolumn = len(rows[0])
            i = 1
            j = 0
            model = QtGui.QStandardItemModel(xrows, xcolumn)
            model.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Date of Change','Comment'])
            for i in range(xrows):
                for j in range(xcolumn):
                    item = QtGui.QStandardItem(str(rows[i][j]))
                    model.setItem(i, j, item)
                    item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
            self.taskListTable.setModel(model)
            filter_proxy_model = QtGui.QSortFilterProxyModel()
            filter_proxy_model.setSourceModel(model)
            filter_proxy_model.setFilterKeyColumn(1)
            filter_proxy_model2 = QtGui.QSortFilterProxyModel()
            filter_proxy_model2.setSourceModel(filter_proxy_model)
            filter_proxy_model2.setFilterKeyColumn(2)
            filter_proxy_model3 = QtGui.QSortFilterProxyModel()
            filter_proxy_model3.setSourceModel(filter_proxy_model2)
            filter_proxy_model3.setFilterKeyColumn(5)
            self.createdByText.textChanged.connect(filter_proxy_model.setFilterRegExp)
            self.taskListTable.setModel(filter_proxy_model)
            self.connect(self.comboBoxTaskStatus,SIGNAL("currentIndexChanged(QString)"),filter_proxy_model2.setFilterRegExp)
            self.taskListTable.setModel(filter_proxy_model2)

            #self.connect(self.dateTimeEdit.text(),SIGNAL("dateChanged(QString)"),filter_proxy_model3.setFilterRegExp)
            #self.dateTimeEdit.dateChanged.connect(filter_proxy_model3.setFilterRegExp)
            #self.taskListTable.setModel(filter_proxy_model3)

    def dateChanged(self):
        try:
                modDate=self.dateTimeEdit.text()
                modDateValue = modDate.upper()
                system="RECS"
                connect =  ConnectionHandler()
                cur = connect.connect_Common()
                cur.execute("select taskid, createdby,status,beginlifespan,endlifespan,comments from v_l1_task where system like '%s' AND MODIFICATIONDATE like '%s'"%(system,modDateValue))
                rows = cur.fetchall()
                print rows
                xrows = len(rows)
                print xrows
                xcolumn = len(rows[0])
                i = 1
                j = 0
                model2 = QtGui.QStandardItemModel(xrows, xcolumn)
                model2.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Comment'])
                for i in range(xrows):
                    for j in range(xcolumn):
                        item = QtGui.QStandardItem(str(rows[i][j]))
                        model2.setItem(i, j, item)
                        item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
                self.taskListTable.setModel(model2)

        except:
            QMessageBox.information(self, "Message", "No Result Found!")
    def rowClicked(self):
        global rows
        global taskID
        model = self.taskListTable.model()
        print model.rowCount()
        #x=model.data(1,1)
        #print str(x)
        indexes = self.taskListTable.selectionModel().selectedRows()

        for index in sorted(indexes):
            rowIndex=index.row()
            index = model.index(rowIndex, 0)
            itm=str(model.data(index))
        taskID = itm
        self.currentTaskLabel.setText("Current Task: "+str(taskID))

        try:
            connect =  ConnectionHandler()
            cur = connect.connect_Common()
            cur.execute(
                "select taskid, createdby,status,beginlifespan,endlifespan,comments from v_l1_task WHERE taskid = '%s'" % (
                    taskID))
            rows = cur.fetchall()
            xrows = len(rows)
            xcolumn = len(rows[0])

            self.propertiesTable.setColumnCount(xrows)
            self.propertiesTable.setRowCount(xcolumn)
            self.propertiesTable.setVerticalHeaderLabels(
                ['TaskID', 'Created By','Status', 'Modified By', 'Creation Date', 'Modification Date', 'Begin Life Span',
                 'End Life Span', 'Task Status', 'Comment'])
            for column in range(xcolumn):
                for row in range(xrows):
                    item = QtGui.QTableWidgetItem(str(rows[row][column]))
                    self.propertiesTable.setItem(row, column, item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)

        except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect!")

    def showTaskAreaClicked(self):
        showTask = showTaskArea()
        showTask.getInitXml(taskID)


    def loadTaskClicked(self,taskID):
        print taskID
        layers = iface.legendInterface().layers()
        for layer in layers:
           if layer.name() == 'TaskLayer':
               QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
        load=LoadTask()
        load.loadXML(taskID)
        connect =  ConnectionHandler()
        cur = connect.connect_Common()
        cur.execute("SELECT dataxml FROM t_task WHERE Taskid = '%s'" % (taskID))
        dataXML = cur.fetchall()[0][0].read()
        dirname = "Z:\\GMLFile\\"
        pathDir = os.path.dirname(dirname)
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)
        save_path = 'Z:\\GMLFile\\'
        name_of_file = str(taskID)
        completeName = os.path.join(save_path, name_of_file+".gml")
        openFile = open(completeName, "w")
        openFile.write(dataXML)
        openFile.close()
        parsedGML = GMLParser()
        parsedGML.createXML(taskID)
        #self.gmlWrite()

        iface.addVectorLayer("Z:\\GMLFile\\ogrGML.gml","gmlToShape","ogr")
        for layer in layers:
           if layer.name() == 'gmlToShape':
             iface.setActiveLayer(layer)
        _vlayer = iface.activeLayer()	
        QgsVectorFileWriter.writeAsVectorFormat(_vlayer,"Z:\\GMLFile\\%s.shp"%(taskID),"utf-8",None,"ESRI Shapefile")
        layers = iface.legendInterface().layers()
        for layer in layers:
            if layer.name() == 'gmlToShape':
                print layer.name()
                QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
		
        #QgsMapLayerRegistry.instance().removeAllMapLayers()
        iface.addVectorLayer("Z:\\GMLFile\\%s.shp"%(taskID),"TaskLayer","ogr")
        vLayer=iface.activeLayer()
        canvas = iface.mapCanvas()
        extent = vLayer.extent()
        canvas.setExtent(extent)
        symbols=vLayer.rendererV2().symbols()
        symbol=symbols[0]
        symbol.setColor(QtGui.QColor.fromRgb(255,248,220))
        vLayer.setLayerTransparency(50)
    def cancelTask(self):
        serviceConnect=ServiceHandler()
        serviceConnect.task_cancel(taskID)
    def taskIDValue(self):
        return taskID
    def featureProperty(self):
        ShowTaskArea=showTaskArea()
        OID=ShowTaskArea.getOID(taskID)
        return OID


