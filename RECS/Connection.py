import cx_Oracle


class ConnectionHandler:
    '''
    This Python function returns the cursor after instantiating connection
    to the local common schema
    '''
    def connect_Common(self):
        con = cx_Oracle.connect('common/common@172.20.0.71:1521/sccdb')
        cur = con.cursor()
        return cur
    def connect_RECS(self):
        con = cx_Oracle.connect('recs/recs@172.20.0.71:1521/sccdb')
        cur = con.cursor()
        return cur
	