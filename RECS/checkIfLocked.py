from Connection import ConnectionHandler
class CheckLocking:

    def isLocked(self,upid):
        connect = ConnectionHandler()
        cur = connect.connect_RECS()
        cur.execute(u"select taskidfk from t_spatialunit where id in( select spatialunitidfk from t_parcel where uniqueparcelid like " + "'%" + upid +"%'" " )"  )
        retval = cur.fetchall()
        if retval[0][0] == None:
            return False
        else:
            return True
