__author__ = 'Robel'
import os
from qgis.core import *
from PyQt4 import QtGui, uic
from qgis.utils import *
from PyQt4.QtGui import QMessageBox
from Connection import ConnectionHandler
from task_manager_dialog import TaskManagerDialog
from ShowTaskArea import showTaskArea
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'UI/feature_property_dialog.ui'))


class featureProperty(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(featureProperty, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.okButton.clicked.connect(self.update)
        self.cancelButton.clicked.connect(self.cancelClicked)

    def populate(self):
        taskMgrDlg=TaskManagerDialog()
        OID=taskMgrDlg.oid_value()
        print OID
        con=ConnectionHandler()
        cur=con.connect_RECS()
        cur.execute(
                "select block_no,street_name,street_no,woredacode, area,area_d,area_m,perimeter,perimeter_d,perimeter_m,beginlifespan,endlifespan,voided,surveyed,uniqueparcelid  from v_l2_parcel where oid='%s'"%(OID))

        fetchedData=cur.fetchall()
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
        self.lineEdit_13.setText(OID)
        self.lineEdit_15.setText(str(fetchedData[0][11]))
        print fetchedData
    def update(self):
        print "ok button clicked"
    def cancelClicked(self):
        self.close()