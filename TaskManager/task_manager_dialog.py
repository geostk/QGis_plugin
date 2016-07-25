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
from RECS.Connection import ConnectionHandler
import os
import cx_Oracle
from PyQt4 import QtCore
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox, QAction,QTableWidget
from PyQt4.QtGui import QMessageBox,QDockWidget
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from gmlParse import GMLParser
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import Qt, SIGNAL
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'task_manager_dialog_base.ui'))


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
        #self.taskListTable.cellClicked.connect(self.rowClicked)
        self.showTaskareaButton.clicked.connect(self.showTaskAreaClicked)
        self.loadfTaskButton.clicked.connect(self.loadTaskClicked)
        #self.refreshTaskButton.clicked.connect(self.populate)

        self.taskListTable.setSelectionBehavior(QTableWidget.SelectRows)
        header = self.taskListTable.horizontalHeader()
        header.setStretchLastSection(True)
        header2 = self.propertiesTable.horizontalHeader()
        header2.setStretchLastSection(True)
        self.taskListTable.verticalHeader().setVisible(False)
        self.propertiesTable.horizontalHeader().setVisible(False)
        self.dateTimeEdit.setCalendarPopup(True)

    def populate(self):

        subsystem='RECS'
        global xrows
        global xcolumn
        global rows
        connect =  ConnectionHandler()
        cur = connect.connect_Common()
        cur.execute("select taskid, createdby,status,beginlifespan,endlifespan,comments from v_l1_task where system like '%s'"%(subsystem))
        rows = cur.fetchall()
        print "hdgfdjgh"
        xrows = len(rows)
        xcolumn = len(rows[0])
        #xcolumn=6
        i = 1
        j = 0
        model = QtGui.QStandardItemModel(xrows, xcolumn)
        model.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Comment'])
        for i in range(xrows):
            for j in range(xcolumn):
                item = QtGui.QStandardItem(str(rows[i][j]))
                model.setItem(i, j, item)
                item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)



        filter_proxy_model = QtGui.QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(1)
        filter_proxy_model2 = QtGui.QSortFilterProxyModel()
        filter_proxy_model2.setSourceModel(filter_proxy_model)
        filter_proxy_model2.setFilterKeyColumn(0)
        # filter_proxy_model2 = QtGui.QSortFilterProxyModel()
        # filter_proxy_model2.setSourceModel(model)
        # filter_proxy_model2.setFilterKeyColumn(0)

        self.connect(self.createByComboBox,SIGNAL("currentIndexChanged(QString)"),filter_proxy_model.setFilterRegExp)
        self.taskListTable.setModel(filter_proxy_model)
        self.taskIDText.textChanged.connect(filter_proxy_model2.setFilterRegExp)
        self.taskListTable.setModel(filter_proxy_model2)
        #self.createByComboBox.textChanged.connect(self.populate2)


        # self.taskListTable.setModel(filter_proxy_model2)

    def populate2(self):
        xcolumn=6

        i = 1
        j = 0
        model = QtGui.QStandardItemModel(xrows, xcolumn)
        model.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Comment'])
        for i in range(xrows):
            for j in range(xcolumn):
                item = QtGui.QStandardItem(str(rows[i][j]))
                model.setItem(i, j, item)
                item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)



        filter_proxy_model = QtGui.QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0) # third column=
        #filter_proxy_model.setFilterKeyColumn(0)
        # line edit for filtering
        #self.connect(self.createByComboBox,SIGNAL("currentIndexChanged(QString)"),filter_proxy_model.setFilterRegExp)

        self.taskListTable.setModel(filter_proxy_model)



    # def populate2(self):
     #    global xcolumn
     #    global columnValue
     #    subsystem='RECS'
     #    global xrows
     #    global rows
     #    try:
    #
     #        connect =  ConnectionHandler()
     #        cur = connect.connect_Common()
     #        cur.execute("select taskid, createdby,status,beginlifespan,endlifespan,comments from v_l1_task where system like '%s'"%(subsystem))
     #        rows = cur.fetchall()
    #
    #
     #        xrows = len(rows)
     #        xcolumn = len(rows[0])
     #        i = 1
     #        j = 0
     #        self.taskListTable.setSortingEnabled(True)
    #
     #        self.taskListTable.setColumnCount(xcolumn)
     #        self.taskListTable.setRowCount(xrows)
     #        self.taskListTable.setHorizontalHeaderLabels(['TaskID','Created By','Status','Valid From Date','Valid To Date','Comment'])
     #        for i in range(xrows):
     #            for j in range(xcolumn):
     #                item = QtGui.QTableWidgetItem(str(rows[i][j]))
     #                self.taskListTable.setItem(i, j, item)
     #                item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEnabled)
    #
     #    except:
     #        QMessageBox.information(self, "Connection Error", "Can't connect to DataBase!")
	# def rowClicked(self):
    #
	# 	global taskID
	# 	indexes = self.taskListTable.selectionModel().selectedRows()
	# 	for index in sorted(indexes):
    #
	# 		row=index.row()
	# 		itm = self.taskListTable.item(row, 0)
	# 	taskID = itm.text()
    #
    #
	# 	self.currentTaskLabel.setText("Current Task: "+str(taskID))
	# 	# itm = self.taskListTable.item(row, column)
	# 	# x = itm.text()
	# 	# QMessageBox.information(self,"hdkjf","%s"%x)
	# 	# import psycopg2
    #
	# 	from suds.client import Client
     #    try:
     #        connstr = ('common/common@172.20.0.71:1521/ccdb')
     #        conn=cx_Oracle.connect(connstr)
    #
    #
    #
     #        # conn = psycopg2.connect("dbname='ncrprs_db' user='postgres' host='172.20.0.71' password='123456'")
     #        cur = conn.cursor()
    #
     #        cur.execute(
     #            "SELECT  taskid, createdby, modifiedby, creationdate, modificationdate, beginlifespan, endlifespan,  comments FROM common.t_task WHERE taskid = '%s'" % (
     #                taskID))
     #        rows = cur.fetchall()
     #        xrows = len(rows)
     #        xcolumn = len(rows[0])
    #
     #        self.propertiesTable.setColumnCount(xrows)
     #        self.propertiesTable.setRowCount(xcolumn)
     #        self.propertiesTable.setVerticalHeaderLabels(
     #            ['TaskID', 'Created By', 'Modified By', 'Creation Date', 'Modification Date', 'Begin Life Span',
     #             'End Life Span', 'Task Status', 'Comment'])
     #        for column in range(xcolumn):
     #            for row in range(xrows):
     #                item = QtGui.QTableWidgetItem(str(rows[row][column]))
     #                self.propertiesTable.setItem(row, column, item)
     #                item.setFlags(QtCore.Qt.ItemIsEnabled)
    #
    #
    #
    #
    #
    #
     #        # self.fId = x
     #        # layer = iface.activeLayer()
     #        # itr = layer.getFeatures()
     #        # ids = []
     #        # self.idd = int(self.fId)
     #        # for i in itr:
     #        #         if self.idd == i.id():
     #        #            ids.append(i.id())
     #        #
     #        #            layer.setSelectedFeatures(ids)
     #        #            box =layer.boundingBoxOfSelected()
     #        #            self.canvas.setExtent(box)
     #        #            self.canvas.refresh()
     #        #            # iface.mapCanvas().setExtent(box)
     #        #            # iface.mapCanvas().refresh()
     #        #
     #        #         else:
     #        #            continue
     #        # extent = QgsRectangle()
     #        # extent.setMinimal()
     #        # layers = [iface.mapCanvas().layers()[1] ]
     #        # for layer in layers:
     #        #   extent.combineExtentWith( layer.extent())
     #        #   self.canvas.setExtent(extent)
     #        #   self.canvas.refresh()
    #
     #    except:
     #        QMessageBox.information(self, "Connection Error", "Unable to Connect!")

    def showTaskAreaClicked(self):
       try:

        self.gmlWrite()
        layers = iface.legendInterface().layers()
        for layer in layers:
          if layer.name() == 'Preview':
              QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
        pLayer = QgsVectorLayer("{HOME}/Documents/GMLFile/parcelGML.gml","Preview","ogr")

        QgsMapLayerRegistry.instance().addMapLayer(pLayer)

        pLayer.selectAll()
        mCanvas = iface.mapCanvas()
        mCanvas.zoomToSelected()
       except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect!")
    def loadTaskClicked(self):

        connstr = ('common/common@172.20.0.71:1521/sccdb')
        conn = cx_Oracle.connect(connstr)
        cur =conn.cursor()
        cur.execute("SELECT dataxml FROM t_task WHERE Taskid = '%s'" % (taskID))
        dataXML = cur.fetchall()[0][0].read()
        dirname = "C:\\Users\\Pc\\Desktop\\GMLFile\\"
        pathDir = os.path.dirname(dirname)
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)
        save_path = 'C:\\Users\\Pc\\Desktop\\GMLFile\\'
        name_of_file = str(taskID)
        completeName = os.path.join(save_path, name_of_file+".gml")
        openFile = open(completeName, "w")
        openFile.write(dataXML)
        openFile.close()
        parsedGML = GMLParser()
        parsedGML.createXML()
        #self.gmlWrite()
        iface.addVectorLayer("C:\\Users\\Pc\\Desktop\\GMLFile\\ogrGML.gml","gmlToShape","ogr")
        layers = iface.legendInterface().layers()        
        for layer in layers:           
           if layer.name() == 'gmlToShape':
             iface.setActiveLayer(layer)
        _vlayer = iface.activeLayer()	
        QgsVectorFileWriter.writeAsVectorFormat(_vlayer,"C:\\Users\\Pc\\Desktop\\GMLFile\\parcel.shp","utf-8",None,"ESRI Shapefile")
        for layer in layers:
            if layer.name() == 'gmlToShape':
                QgsMapLayerRegistry.instance().removeMapLayer(layer.id())

        #QgsMapLayerRegistry.instance().removeAllMapLayers()
        iface.addVectorLayer("C:\\Users\\Pc\\Desktop\\GMLFile\\parcel.shp","ParcelWithNeighbour","ogr")





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
            # url="http://172.20.85.48/wcfService1/Service1.svc?wsdl"
            url="http://172.20.0.71/TPFProxy/TPFProxyTaskManagerService.svc?wsdl"
            client=Client(url)
            gml=client.service.LoadTaskData(taskID,subSystem)


            # conn = psycopg2.connect("dbname='ncrprs_db' user='postgres' host='172.20.0.71' password='123456'")
            # cur = conn.cursor()
            #
            # cur.execute(
            #     """SELECT dataxml FROM common.t_task WHERE id = '%d'"""%(5221))
            # gml = cur.fetchall()
            save_path = '{HOME}/Documents/GMLFile/'
            name_of_file = "parcelGML"
            completeName = os.path.join(save_path,name_of_file+".gml")
            openFile = open(completeName, "w")
            # openFile.write(" ".join([" ".join(v) for v in gml]))
            openFile.write(gml)
            openFile.close()
        except:
            QMessageBox.information(self, "Connection Error", "Unable to Connect to Service")

