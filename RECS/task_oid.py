__author__ = 'Rob-G'
from Connection import ConnectionHandler
class FeatureTask:
    def taskOid(self,taskid):
        con = ConnectionHandler()
        cur = con.connect_Common()
        cur.execute("select INITXML from T_TASK where TASKID = '%s'" % (taskid))
        rows = cur.fetchall()
        xmlData = rows[0][0].read()
        # y="""<?xml version="1.0" encoding="utf-8"?><InitTask xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://hansaluftbild.de/InitTaskTPF.xsd"><Metadata><SystemName>RECS</SystemName><TPFProxyId>Bole</TPFProxyId></Metadata><Task><TASKID>Bole-1003</TASKID><CREATEDBY>yarecs</CREATEDBY><MODIFIEDBY>yarecs</MODIFIEDBY><CREATIONDATE>2016-06-30T17:05:20.3064695+03:00</CREATIONDATE><MODIFICATIONDATE>2016-06-30T17:05:20.3064695+03:00</MODIFICATIONDATE><BEGINLIFESPAN>2016-06-30</BEGINLIFESPAN><TRANSACTIONTYPEIDFK>14</TRANSACTIONTYPEIDFK><TaskObject><Type>Parcel</Type><ExistingObjectIdentifier><OID>ETH0001000000-00000157677</OID><BEGINLIFESPAN>2012-03-30</BEGINLIFESPAN><ENDLIFESPAN>3000-12-31</ENDLIFESPAN></ExistingObjectIdentifier><ExistingObjectIdentifier><OID>ETH0001000000-00000157674</OID><BEGINLIFESPAN>2012-03-30</BEGINLIFESPAN><ENDLIFESPAN>3000-12-31</ENDLIFESPAN></ExistingObjectIdentifier></TaskObject><COMMENTS /><SubCityCode>06</SubCityCode></Task></InitTask>"""
        #xmlDoc = ET.fromstring(y)
        import xml.dom.minidom
        doc = xml.dom.minidom.parseString(xmlData);
        parcels = doc.getElementsByTagName("ExistingObjectIdentifier")
        lst_oid=[]
        for parcel in parcels:
            OID = parcel.getElementsByTagName('OID')[0]
            OIDValue = OID.childNodes[0].data
            lst_oid.append(OIDValue)
        #print len(lst_oid)
        return lst_oid
		

    def populate(self,oid):
        print "xx"

    if __name__ == "__main__":
        taskOid()
