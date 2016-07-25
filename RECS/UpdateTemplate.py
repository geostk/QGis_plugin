from Connection import ConnectionHandler
import xml.etree.ElementTree as ET
import datetime
import time
from suds.client import Client
from InitTaskForward import InitTaskForward
class FinishTask:

    def getAdminData(self,taskId):
        connect = ConnectionHandler()
        cur = connect.connect_Common()
        cur.execute(u"select createdby,modifiedby, creationdate,modificationdate  from t_task where taskid = '%s'" % (taskId) )
        retval = cur.fetchall()
        return retval[0]

    def getParcelType(self,uiParcelTypeChoosed):
        con = ConnectionHandler()
        cur = con.connect_RECS()
        cur.execute("select id from t_parceltype where parceltype = '%s'" % (uiParcelTypeChoosed))
        retval = cur.fetchall()
        return retval[0][0]

    def getOldOid(self,taskid):
        con = ConnectionHandler()
        cur = con.connect_Common()
        cur.execute("select INITXML from T_TASK where TASKID = '%s'" % (taskid))
        rows = cur.fetchall()
        xmlData = rows[0][0].read()
        print xmlData
        xmlDoc = ET.fromstring(xmlData)
        print xmlDoc
        oid = (xmlDoc[1][7])[1][0].text
        bls = (xmlDoc[1][7])[1][1].text
        els = (xmlDoc[1][7])[1][2].text
        return [oid,bls,els]

    def getNewOid(self):
        con = ConnectionHandler()
        cur = con.connect_Common()
        cur.execute("select OID_SEQ.nextval from DUAL")
        retval = cur.fetchall()
        return 'ETH0001006000-'+ '{:011d}'.format(retval[0][0])

    def getSizeData(self,oid):
        connect = ConnectionHandler()
        cur = connect.connect_RECS()
        cur.execute(u"select area,perimeter from t_parcel where spatialunitidfk in (select id from t_spatialunit where oid = '%s')"%(str(oid)))
        retval = cur.fetchall()
        return retval[0]

    def CDATA(self,text=None):
        """
        A CDATA element factory function that uses the function itself as the tag
        (based on the Comment factory function in the ElementTree implementation).
        """
        element = ET.Element("CDATA")
        element.text = ''
        return element.text

    def TransactionUpdateXML(self,taskId,parceltype,str_name,a_m,a_d,p_m,p_d):
        f= FinishTask()
        adminData =  f.getAdminData(taskId)
        print adminData
        createdby = adminData[0]
        modifiedby = adminData[1]
        creationDate = '2015-12-04T17:17:03.3138385+03:00'
        print creationDate
        modificationDate = '2015-12-04T17:17:03.3138385+03:00'
        print modificationDate
        ogcdata =  '<![CDATA[]]>'
        print type(ogcdata)
        # print ogcdata
        typeId = f.getParcelType(parceltype)
        OldID = f.getOldOid(taskId)
        Ooid = OldID[0]
        OBls = OldID[1]
        OEls = OldID[2]
        nOid = f.getNewOid()
        nBls = time.strftime('%Y-%m-%d')
        nEls = OEls
        area = f.getSizeData(Ooid)[0]
        # print type(area)
        perimeter = f.getSizeData(Ooid)[1]

        x =  """<?xml version="1.0"?><Transaction xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://hansaluftbild.de/RECSTransaction.xsd">
        <TransactionHeader>
        <Metadata>
        <SystemName>RECS</SystemName>
        </Metadata>
        <Task>
        <TaskIdentifier>%s</TaskIdentifier>
        <COMMENTS/>
        </Task>
        </TransactionHeader>
        <New/>
        <Update>
        <Features xsi:type="ParcelType">
        <Administration>
        <CreatedBy>%s</CreatedBy>
        <ModifiedBy>%s</ModifiedBy>
        <CreationDate>%s</CreationDate>
        <ModificationDate>%s</ModificationDate>
        </Administration>
        <OGC_GEOMETRY>%s</OGC_GEOMETRY>
        <TypeId>%s</TypeId>
        <UpdateFeatureData>
        <OldIdentifier>
        <OID>%s</OID>
        <BEGINLIFESPAN>%s</BEGINLIFESPAN>
        <ENDLIFESPAN>%s</ENDLIFESPAN>
        </OldIdentifier>
        <NewIdentifier>
        <OID>%s</OID>
        <BEGINLIFESPAN>%s</BEGINLIFESPAN>
        <ENDLIFESPAN>%s</ENDLIFESPAN>
        </NewIdentifier>
        <PointX>474675.686002583</PointX>
        <PointY>992085.822097618</PointY>
        </UpdateFeatureData>
        <Surveyed>false</Surveyed>
        <Street_name>%s</Street_name>
        <City/>
        <StreetName/>
        <StreetNumber/>
        <HouseNumber/>
        <Area>%s</Area>
        <Area_m>%s</Area_m>
        <Area_d>%s</Area_d>
        <Perimeter>%s</Perimeter>
        <Perimeter_m>%s</Perimeter_m>
        <Perimeter_d>%s</Perimeter_d>
        </Features>
        </Update>
        <Void/>
        </Transaction>
        """%(taskId,createdby,modifiedby,creationDate,modificationDate,ogcdata,typeId,Ooid,OBls,OEls,nOid,nBls,nEls,str_name,area,a_m,a_d,perimeter,p_m,p_d)
        return x


