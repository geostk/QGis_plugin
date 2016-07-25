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
from ShowTaskArea import showTaskArea
from PyQt4.QtCore import SIGNAL
from gmlToShape import GmlToShape
from task_info_dialog import taskInfo
from task_oid import FeatureTask
from feature_curent_task_dialog import taskFeatures
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
		
        self.taskListTable.clicked.connect(self.rowClicked)
        self.showTaskareaButton.clicked.connect(self.showTaskAreaClicked)
        self.loadfTaskButton.clicked.connect(self.loadTaskClicked)
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
            #value='--Select--'
            #index = self.comboBoxTaskStatus.findData(value)
            index=0
            self.comboBoxTaskStatus.setCurrentIndex(index)
            self.createdByText.clear()
            self.taskidText.clear()
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
            filter_proxy_model3.setFilterKeyColumn(0)
            self.createdByText.textChanged.connect(filter_proxy_model.setFilterRegExp)
            self.taskListTable.setModel(filter_proxy_model)
            self.connect(self.comboBoxTaskStatus,SIGNAL("currentIndexChanged(QString)"),filter_proxy_model2.setFilterRegExp)
            self.taskListTable.setModel(filter_proxy_model2)

            #self.connect(self.dateTimeEdit.text(),SIGNAL("dateChanged(QString)"),filter_proxy_model3.setFilterRegExp)
            self.taskidText.textChanged.connect(filter_proxy_model3.setFilterRegExp)
            #self.dateTimeEdit.dateChanged.connect(filter_proxy_model3.setFilterRegExp)
            self.taskListTable.setModel(filter_proxy_model3)
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
        #self.currentTaskLabel.setText("Current Task: "+str(taskID))

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
                ['TaskID', 'Created By','Status', 'Begin Life Span', 'End Life Span', 'Comment'])
            for column in range(xcolumn):
                for row in range(xrows):
                    item = QtGui.QTableWidgetItem(str(rows[row][column]))
                    self.propertiesTable.setItem(row, column, item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)

        except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect!")
    def showTaskAreaClicked(self):
        try:
            showTask = showTaskArea()
            showTask.getInitXml(taskID)
        except:
             QMessageBox.information(self, "CMessage", "Unable to to show task area!")
    def showTaskInfo(self):
        obj = taskInfo()
        obj.getAttribData()
    def loadTaskClicked(self):
        layers = iface.legendInterface().layers()
        for layer in layers:
           if layer.name() == 'TaskLayer':
               QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
        gmlShape=GmlToShape()
        gmlShape.createShape(taskID)
        iface.addVectorLayer("Z:\\GMLFile\\%s.shp"%(taskID),"TaskLayer","ogr")
        vLayer=iface.activeLayer()
        canvas = iface.mapCanvas()
        extent = vLayer.extent()
        canvas.setExtent(extent)
        symbols=vLayer.rendererV2().symbols()
        symbol=symbols[0]
        symbol.setColor(QtGui.QColor.fromRgb(255,248,220))
        vLayer.setLayerTransparency(50)
        featuresOfTask=FeatureTask()
        lst_oid=featuresOfTask.taskOid(taskID)
        # vLayer.setSelectedFeatures(lst_oid)
        #len_lst=len(lst_oid)
        lst_fid=[]
        for oids in lst_oid:
            for x in vLayer.getFeatures():
                attrs = x.attributes()
                if attrs[1]==oids:
                    lst_fid.append(attrs[6]-1)

        vLayer.setSelectedFeatures(lst_fid)
        import  pickle
        import logging
        f2 = open('Z:\session','rb')
        user = pickle.load(f2)
        gmlShape=GmlToShape()
        gmlShape.createShape(taskID)
        logging.basicConfig(format='%(asctime)s %(message)s',filename='Z:\Log\AACADIS.RECS.log_%s'%user,level=logging.INFO)
        logging.info('Task Loaded successfully from Task Manager TableGrid - TaskID:%s'%taskID)
        self.currentTaskLabel.setText("Current Task: "+str(taskID))
        # fetureTaskmgr=taskFeatures()
        # fetureTaskmgr.populate(taskID)
        # mCanvas = iface.mapCanvas()
        # mCanvas.zoomToSelected()
    def cancelTask(self):
        serviceConnect=ServiceHandler()
        serviceConnect.task_cancel(taskID)
        QMessageBox.information(self, "Message", "Task Successfully Canceled!")

    def retTaskID(self):
        return taskID
