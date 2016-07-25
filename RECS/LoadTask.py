from Connection import ConnectionHandler
import pickle

from ServiceHandler import ServiceHandler
class LoadTask:

     def loadXML(self,taskID):
         newTask = ServiceHandler()
         newTask.task_load(taskID)




