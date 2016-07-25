__author__ = 'Devazil'

import xml.etree.ElementTree as ET
from PyQt4.QtSql import *
from PyQt4.QtGui import QMessageBox
from Connection import ConnectionHandler
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtSql import *
class showTaskArea():
    def getInitXml(self,taskid):
        con = ConnectionHandler()
        cur = con.connect_Common()
        cur.execute("select INITXML from T_TASK where TASKID = '%s'" % (taskid))
        rows = cur.fetchall()
        xmlData = rows[0][0].read()
        print xmlData
        xmlDoc = ET.fromstring(xmlData)
        task = (xmlDoc[1][7])[1][0].text

        # print task
        self.getUpi(task)

    def getUpi(self,Oid):
        con = ConnectionHandler()
        cur = con.connect_RECS()
        cur.execute("select id from t_spatialunit where oid = '%s'" % (Oid))
        id = cur.fetchall()
        ids=id[0][0]
        cur.execute("select uniqueparcelid from t_parcel where spatialunitidfk in '%s'" % (ids))
        upi = cur.fetchall()
        upiV=upi[0][0]
        # print upiV
        self.zoomtoUPID(upiV)

    # Method use for zoom to selected layer by parcel ID(Technichal ID)
    def zoomtoUPID(self,upid):
        try:
            connect = ConnectionHandler()
            cur = connect.connect_RECS()
            cur.execute("SELECT ID FROM RECS.T_PARCEL WHERE UNIQUEPARCELID = '%s'" % (upid))
            ID = cur.fetchall()
            if not ID:
                QMessageBox.information(self, "Invalid Parcel ID", "Invalid Unique Parcel ID !")
                return

            ids = []
            ids.append(ID[0][0])
            # print ids
            layers = iface.legendInterface().layers()  # All the Layers
            for layer in layers: # Extract the parcel layer from the given layers
                if layer.name() == 'PARCEL':
                    iface.setActiveLayer(layer)
            active_layer = iface.activeLayer()
            # print active_layer.name()
            active_layer.setSelectedFeatures(ids)
            mCanvas = iface.mapCanvas()
            mCanvas.zoomToSelected()

        except:
            print "There is an Exception !!"
   
