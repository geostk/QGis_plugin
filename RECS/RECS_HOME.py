# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectTask
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
import os
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QMessageBox,QDockWidget
from PyQt4 import QtGui, uic
from PyQt4 import QtCore
from PyQt4.QtGui import QMenu
import sys
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import aacadisicon

# Import the code for the dialog
from Select_Task_dialog import SelectTaskDialog
from Log_In_dialog import LogInDialog
from task_manager_dialog import TaskManagerDialog
from task_info_dialog import taskInfo
#from map_loader_dialog import LoadMapDialog
from init_task_dialog import InitTaskDialog
from PyQt4.QtGui import QMessageBox,QAction
import os.path
import xml.dom.minidom
from GeometyEdit import GeometryEdit
from feature_curent_task_dialog import  taskFeatures

class RECS:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'RECS_HOME_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.initdlg=InitTaskDialog()
        self.selectdlg = SelectTaskDialog()
        self.loginDlg=LogInDialog()
        self.taskMgrDlg=TaskManagerDialog()
        self.taskInfoDlg=taskInfo()
        self.taskFeaturesDlg=taskFeatures()
        #self.loadmapDlg=LoadMapDialog()
        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Task')
        self.logIn()
        self.selectTask()
        self.actions = []

        self.toolbar = self.iface.addToolBar(u'Recs')
        self.toolbar.setObjectName(u'Recs')


        # layer.editingStarted.connect(editLayer() )




        # TODO: We are going to let the user set this up in a future iteration
        #self.toolbar = self.iface.addToolBar(u'SelectTask')
        #self.toolbar.setObjectName(u'SelectTask')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Tasks', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            # self.menu = QMenu( "&Task", self.iface.mainWindow().menuBar() )
            action = self.iface.mainWindow().menuBar().actions()
            lastAction = action[-1]
            self.iface.addPluginToMenu(
                self.menu,
                lastAction)

        self.actions.append(lastAction)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        """ Task menu setting """
        self.menu = QMenu(self.iface.mainWindow())
        self.menu.setObjectName("task_menu_object")
        self.menu.setTitle("Task")





        """ Task """
        self.action_tasks = QAction(QIcon('::/plugins/RECS/aacadisicon.png'), "Tasks", self.iface.mainWindow())
        self.action_tasks.setObjectName("Task_action_object")
        self.action_tasks.setWhatsThis("Task Initialized")
        #QtCore.QObject.connect(self.action_tasks, SIGNAL("triggered()"), self.tasks)

        """ Initializing Task """
        self.action_init_task = QAction(QIcon('::/plugins/RECS/aacadisicon.png'), "Initialize ", self.iface.mainWindow())
        self.action_init_task.setObjectName("Task_action_object")
        self.action_init_task.setWhatsThis("Task Initialize")
        QtCore.QObject.connect(self.action_init_task, SIGNAL("triggered()"), self.initTask)


        """ Select Task """
        self.action_select_task = QAction(QIcon(':/plugins/RECS/aacadisicon.png'), "Select Task", self.iface.mainWindow())
        self.action_select_task.setObjectName("Task_Select_object")
        self.action_select_task.setWhatsThis("Select Task")
        QtCore.QObject.connect(self.action_select_task, SIGNAL("triggered()"), self.selectTask)

        """ Reload Task """
        self.action_reload_task = QAction(QIcon(':/plugins/RECS/aacadisicon.png'), "Reload Task", self.iface.mainWindow())
        self.action_reload_task.setObjectName("Task_Reload_object")
        self.action_reload_task.setWhatsThis("Reload Task")
        QtCore.QObject.connect(self.action_reload_task, SIGNAL("triggered()"), self.taskManager)

        """ Edit Task """
        self.action_edit_task = QAction(QIcon(':/plugins/RECS/aacadisicon.png'), "Edit Task", self.iface.mainWindow())
        self.action_edit_task.setObjectName("Task_Edit_object")
        self.action_edit_task.setWhatsThis("Edit Task")
        QtCore.QObject.connect(self.action_edit_task, SIGNAL("triggered()"), self.editLayer)


        """ Finish Task """
        self.action_finish_task = QAction(QIcon(':/plugins/RECS/aacadisicon.png'), "Finish Task", self.iface.mainWindow())
        self.action_finish_task.setObjectName("Task_Finish_object")
        self.action_finish_task.setWhatsThis("Edit Task")
        QtCore.QObject.connect(self.action_finish_task, SIGNAL("triggered()"), self.finishEditngLayer)


        """ Add action to the menu list """
        #self.menuTask.addAction(self.action_tasks)

        self.menu.addAction(self.action_init_task)
        self.menu.addAction(self.action_select_task)
        self.menu.addAction(self.action_reload_task)
        self.menu.addAction(self.action_edit_task)
        self.menu.addAction(self.action_finish_task)

        """ Add menu to the menubar """
        menubar=self.iface.mainWindow().menuBar()
        menubar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.menu)



        """ Add icon to the toolbar """
        #self.iface.addPluginToMenu(u"&load Map", self.action_loadmap)
        #self.iface.addToolBarIcon(self.action_init_task)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Task_Manager'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
    def initTask(self):

        layers = self.iface.legendInterface().layers()
        #layer_list = []
        for layer in layers:
           #layer_list.append(layer.name())
           if layer.name() == 'PARCEL':
            self.iface.setActiveLayer(layer)
        self.initdlg.show()
        #layer_list=list(set(layer_list))
        #self.initdlg.comboBox.addItems(layer_list)
        self.initdlg.setFixedSize(self.initdlg.size())
        result = self.initdlg.exec_()
        if result:
            pass
    def selectTask(self):
        self.selectdlg.show()
        self.selectdlg.setFixedSize(self.selectdlg.size())

        self.selectdlg.loadLayer()
        self.selectdlg.populate()
        result = self.selectdlg.exec_()
        if result:
            # self.selectdlg.close()
            pass
    def showTaskInfo(self):
        self.taskInfoDlg.show()
        t_id = self.taskMgrDlg.retTaskID()
        self.taskInfoDlg.getAttribData(t_id)
        #self.taskInfoDlg.populate()
    def taskManager(self):

        if self.taskMgrDlg.isVisible():
            self.taskMgrDlg.loadTaskClicked()
            # self.taskMgrDlg.close()
            # self.apdockwidget.close()
        else:
            self.taskMgrDlg.show()
            self.apdockwidget = QDockWidget("Task Manager", self.iface.mainWindow())
            self.apdockwidget.setWindowFlags(Qt.FramelessWindowHint)
            self.apdockwidget.setWidget(self.taskMgrDlg)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.apdockwidget)
            self.taskMgrDlg.populate()
            self.taskFeatures()




        # rows = self.taskMgrDlg.taskListTable.rowCount()
        # createdByList=[]
        #
        #
        # for row in range(0,rows):
        #     createdByItems=self.taskMgrDlg.taskListTable.item(row,1)
        #     createdByList.append(createdByItems.text())
        #
        #
        # createdByList=list(set(createdByList))
        # self.taskMgrDlg.createByComboBox.addItems(createdByList)
        # self.taskMgrDlg.createByComboBox.setCurrentIndex(createdByList.index())
        self.menu = QtGui.QMenu()
        #newTask=self.menu.addAction("New Task",self.newTask,"")
        newTask = self.menu.addAction("New Task", self.newTaskEvent)
        loadTask = self.menu.addAction("Load Task", self.loadTaskEvent)
        cancelTask = self.menu.addAction("Cancel Task", self.cancelTaskEvent)
        showTaskArea = self.menu.addAction("Show Task Area", self.showTaskAreaEvent)
        noTask=self.menu.addAction("No Task",self.noTaskEvent)
        showTaskInfo=self.menu.addAction("Show Task Info",self.showTaskInfoEvent)
        updateFeature=self.menu.addAction("Update Features",self.updateFeatureEvent)

        self.taskMgrDlg.taskListTable.addAction(newTask)
        self.taskMgrDlg.taskListTable.addAction(loadTask)
        self.taskMgrDlg.taskListTable.addAction(cancelTask)
        self.taskMgrDlg.taskListTable.addAction(showTaskArea)
        self.taskMgrDlg.taskListTable.addAction(noTask)
        self.taskMgrDlg.taskListTable.addAction(showTaskInfo)
        self.taskMgrDlg.taskListTable.addAction(updateFeature)
        self.taskMgrDlg.taskListTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.taskMgrDlg.taskListTable.customContextMenuRequested.connect(self.contextMenuEvent)
        result = self.taskMgrDlg.exec_()
        if result:
            self.taskMgrDlg.populate()
        #self.connect(self.dateTimeEdit,SIGNAL("dateTimeChange
    def contextMenuEvent(self, point):
        self.menu.exec_(self.taskMgrDlg.taskListTable.mapToGlobal(point))
    def newTaskEvent(self):
        self.initTask()
    def loadTaskEvent(self):
        self.taskMgrDlg.loadTaskClicked()
        t_id = self.taskMgrDlg.retTaskID()
        self.taskFeaturesDlg.populate(t_id)
    def cancelTaskEvent(self):
        self.taskMgrDlg.cancelTask()
    def showTaskAreaEvent(self):
        self.taskMgrDlg.showTaskAreaClicked()
    def noTaskEvent(self):
        print "noTask Called"
    def showTaskInfoEvent(self):
        self.showTaskInfo()
    def updateFeatureEvent(self):
        print "updateFeature"
    def logIn(self):

        self.loginDlg.show()
        self.loginDlg.setWindowFlags(Qt.FramelessWindowHint)
        result = self.loginDlg.exec_()
        if result:
            pass
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
    def editLayer(self):
        global taskLayer
        global featCount
        layers = self.iface.legendInterface().layers()
        for layer in layers:
            if layer.name() == 'TaskLayer':
                taskLayer = layer
                taskLayerID=layer.id()
                self.iface.setActiveLayer(taskLayer)
        featCount = taskLayer.featureCount()
        print featCount
        taskLayer.startEditing()
        QgsProject.instance().setSnapSettingsForLayer(taskLayerID,True,2,1,20,True)
    def finishEditngLayer(self):

        """
        change the edits to GML again to detect the changes

        """
        print featCount
        taskLayer_shape = iface.activeLayer()
        QgsVectorFileWriter.writeAsVectorFormat(taskLayer_shape,"Z:\\GMLEdited\\temp.gml","utf-8",None,"GML")

        #QgsMapLayerRegistry.instance().removeAllMapLayers()
        iface.addVectorLayer("Z:\\GMLEdited\\temp.gml","EditedTaskLayer","ogr")
        """
        Compare the two gml geometries
        """

        doc_edited = xml.dom.minidom.parse("Z:\\GMLEdited\\temp.gml")
        doc_origion = xml.dom.minidom.parse("Z:\\GMLFile\\ogrGML.gml")
        editedParcel = doc_edited.getElementsByTagName("gml:featureMember")
        epLength = editedParcel.length
        print epLength
        obj = GeometryEdit()
        if epLength > featCount:
           obj.split(doc_edited,doc_origion)
           print "split"
        elif epLength < featCount:
            obj.merge(doc_edited,doc_origion)
            print "merge"
        else:
            obj.updateGeom()
            print "update"
    def taskFeatures(self):
        self.taskFeaturesDlg.show()
        self.apdockwidget = QDockWidget("Features Of Current Task", self.iface.mainWindow())
        self.apdockwidget.setWindowFlags(Qt.FramelessWindowHint)
        self.apdockwidget.setWidget(self.taskFeaturesDlg)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.apdockwidget)


        self.menu_feature = QtGui.QMenu()
        #newTask=self.menu.addAction("New Task",self.newTask,"")
        editAttr = self.menu_feature.addAction("Edit", self.editEvent)
        self.taskFeaturesDlg.currentTaskTable.addAction(editAttr)
        self.taskFeaturesDlg.currentTaskTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.taskFeaturesDlg.currentTaskTable.customContextMenuRequested.connect(self.contextMenuEvent2)

        #self.connect(self.dateTimeEdit,SIGNAL("dateTimeChange
    def contextMenuEvent2(self, point):
        self.menu_feature.exec_(self.taskFeaturesDlg.currentTaskTable.mapToGlobal(point))
    def editEvent(self):
        self.showTaskInfo()
