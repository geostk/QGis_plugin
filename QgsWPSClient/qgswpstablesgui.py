# -*- coding: utf-8 -*-
"""
***************************************************************************
   QGIS Web Processing Service Plugin
  -------------------------------------------------------------------
 Date                 : 28 April 2015
 Copyright            : (C) 2015 by Gérald Fenoy
 email                : gerald dot fenoy at geoalbs dot fr

  ***************************************************************************
  *                                                                         *
  *   This program is free software; you can redistribute it and/or modify  *
  *   it under the terms of the GNU General Public License as published by  *
  *   the Free Software Foundation; either version 2 of the License, or     *
  *   (at your option) any later version.                                   *
  *                                                                         *
  ***************************************************************************
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from QgsWPSClient import version
from Ui_qgswpstablesgui import Ui_QgsWpsTablesGUI
import os, sys, string

class QgsWpsTablesGui(QDialog, QObject, Ui_QgsWpsTablesGUI):
  MSG_BOX_TITLE = "QGIS WPS Client"
  
  def __init__(self, parent, fl):
    QDialog.__init__(self, parent, fl)
    self.setupUi(self)
    self.setWindowTitle('QgsWPSClient-'+version()+': tables list')
    self.treeView = QTreeView()
    self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
    self.treeView.customContextMenuRequested.connect(self.openMenu)
    self.model = QStandardItemModel()
    self.treeView.setModel(self.model)
    self.model.setHorizontalHeaderLabels([self.tr("Tables")])
    layout = QVBoxLayout()
    layout.addWidget(self.treeView)
    self.setLayout(layout)
    self.dlgTables={}
    self.selectedServiceName = parent.cmbConnections.currentText()

  def bindTableDisplay(self,dlgTable,layer,file):
    self.dlgTables[layer]={"file":file,"dlgTable":dlgTable}
    
  def addItems(self, parent, elements):
    for text, children in elements:
      item = QStandardItem(text)
      parent.appendRow(item)
      if children:
        self.addItems(item, children)
        
  def openMenu(self, position):
    indexes = self.treeView.selectedIndexes()
    if len(indexes) > 0:
      level = 0
      index = indexes[0]
      while index.parent().isValid():
        index = index.parent()
        level += 1
    menu = QMenu()
    if level == 0:
      openAction = menu.addAction(self.tr("Open"))
      closeAction = menu.addAction(self.tr("Close"))
      saveAction = menu.addAction(self.tr("Save"))
      removeAction = menu.addAction(self.tr("Remove"))

    action=menu.exec_(self.treeView.viewport().mapToGlobal(position))
    if action == openAction:
      for i in range(len(indexes)):
        print >> sys.stderr, "Open file "+str(indexes[i].data())+" ..."
        self.dlgTables[indexes[i].data()]["dlgTable"].show()
    if action == closeAction:
      for i in range(len(indexes)):
        print >> sys.stderr, "Close file "+str(indexes[i].data())+" ..."
        self.dlgTables[indexes[i].data()]["dlgTable"].close()
    if action == saveAction:
      for i in range(len(indexes)):
        print >> sys.stderr, "Safe file "+str(indexes[i].data())+" ..."
        text = open(self.dlgTables[indexes[i].data()]["file"], 'r').read()
        fileName = QFileDialog().getSaveFileName()
    if action == removeAction:
      for i in range(len(indexes)):
        print >> sys.stderr, "Remove file "+str(indexes[i].data())+" ..."
        try:
          unlink(self.dlgTables[indexes[i].data()]["file"])
        except:
          pass
        print >> sys.stderr,dir(indexes[i].row())

  def currentServiceName(self):
      return self.selectedServiceName 
