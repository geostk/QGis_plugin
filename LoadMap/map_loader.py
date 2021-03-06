# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadMap
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
#from map_loader_dialog import LoadMapDialog
import os.path
import time
import thread
import time
from qgis.gui import  *
from qgis.core import *

class LoadMap:
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
            'LoadMap_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
       # self.dlg = LoadMapDialog()
        # self.loadLayer()
        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&map loader')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'LoadMap')
        self.toolbar.setObjectName(u'LoadMap')
        
        

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
        return QCoreApplication.translate('LoadMap', message)

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
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        


        icon_path = ':/plugins/LoadMap/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Load Map'),
            callback=self.run,
            parent=self.iface.mainWindow())


        
    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&map loader'),
                action)
            self.iface.removeToolBarIcon(action)

    
    def run(self):
        """Run method that performs all the real work"""
        self.loadLayer()
    def loadLayer(self):
        self.mlr = None
        QgsMapLayerRegistry.instance().removeAllMapLayers()
        self.mlr = QgsMapLayerRegistry.instance()
        uri = QgsDataSourceURI()
        uri.setConnection("172.20.0.71", "1521", "sccdb", "recs", "recs")
        uri.setDataSource("recs", "T_PARCEL", "GEOMETRY")
        vlayer = QgsVectorLayer(uri.uri(), "Parcel", "ORACLE")
        if vlayer.isValid():
            self.mlr.addMapLayer(vlayer)
        else:
            QMessageBox.information(None, "Unable to Laod Data", "Unable to Load Layers from the Database!")
            
            
    
