__author__ = 'Robel'
from Connection import ConnectionHandler
from LoadTask import LoadTask
from gmlParse import GMLParser
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
import os
from PyQt4 import QtGui
class GmlToShape():
    def createShape(self,taskID):
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
        layers=iface.legendInterface().layers()
        for layer in layers:
           if layer.name() == 'gmlToShape':
             iface.setActiveLayer(layer)
        _vlayer = iface.activeLayer()
        QgsVectorFileWriter.writeAsVectorFormat(_vlayer,"Z:\\GMLFile\\%s.shp"%(taskID),"utf-8",None,"ESRI Shapefile")
        layers = iface.legendInterface().layers()
        for layer in layers:
            if layer.name() == 'gmlToShape':
                #print layer.name()
                QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
