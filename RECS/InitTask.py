from Connection import ConnectionHandler
import pickle

from ServiceHandler import ServiceHandler
class InitXML:

    def query_Oracle(self,upid):
        connect = ConnectionHandler()
        cur = connect.connect_RECS()
        cur.execute(u"select oid,beginlifespan,endlifespan  from t_spatialunit where id in ( select spatialunitidfk from t_parcel where uniqueparcelid like " + "'%" + upid +"%'" " )"  )
        retval = cur.fetchall()
        return retval

    def makeintXML(self,upid,comment):
        initTaskXML = InitXML()
        strval = initTaskXML.query_Oracle(upid)
        oid =  strval[0][0]
        beginlifespan = strval[0][1].date()
        endlifespan = strval[0][2].date()
        f2 = open('Z:\session','rb')
        user = pickle.load(f2)
        xmlString = '<?xml version="1.0" encoding="utf-8" ?><InitTask xmlns="http://hansaluftbild.de/InitTaskClient.xsd"><Metadata><SystemName>RECS</SystemName></Metadata><Task><CREATEDBY>%s</CREATEDBY><MODIFIEDBY>Ras</MODIFIEDBY><TRANSACTIONTYPEIDFK>14</TRANSACTIONTYPEIDFK><TaskObject><Type>Parcel</Type><ExistingObjectIdentifier><OID>%s</OID><BEGINLIFESPAN>%s</BEGINLIFESPAN><ENDLIFESPAN>%s</ENDLIFESPAN></ExistingObjectIdentifier></TaskObject><COMMENTS>%s</COMMENTS><SubCityCode>06</SubCityCode></Task></InitTask>'%(user,oid,beginlifespan,endlifespan,comment)
        newTask = ServiceHandler()
        taskID = newTask.task_forward(xmlString)
        return taskID


