import cx_Oracle
import string
import os
import sys


from suds.client import Client
#header_val={'Content-Type': 'application/soap+xml; charset="UTF-8"'}
#
class ServiceHandler:
    def task_forward(self,strXML):
        client = Client('http://localhost:9001/TPFProxyTaskManagerService.svc/meta?wsdl')
        result = client.service.InitTask(strXML)
        return result
    def task_load(self,taskId):
        client = Client('http://localhost:9001/TPFProxyTaskManagerService.svc/meta?wsdl')
        result = client.service.LoadTaskData(taskId)
        return result
    def task_cancel(self,taskId):
        client = Client('http://localhost:9001/TPFProxyTaskManagerService.svc/meta?wsdl')
        result = client.service.CancelTask(taskId)
        return result
