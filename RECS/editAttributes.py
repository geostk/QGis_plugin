from suds.client import Client
from UpdateTemplate import FinishTask




class EditAttributes():
    def ProcessEdit(self,taskID,parcelType,streetName,a_d,a_m,p_d,p_m):
        obj = FinishTask()
        transXML =  obj.TransactionUpdateXML(taskID,parcelType,streetName,a_d,a_m,p_d,p_m)
        print transXML
        client = Client('http://localhost:9001/TPFProxyTaskManagerService.svc/meta?wsdl')
        result = client.service.StoreChanges(taskID,transXML)
        result = client.service.StoreFinalData(taskID,transXML)
        result = client.service.AcceptTaskData(taskID)
        return  result



