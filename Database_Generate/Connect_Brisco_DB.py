
import psycopg2

class Connect_DB:

    def __init__(self,dbname,user,host,psswrd):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.psswrd = psswrd
    def cnct(self):
        connection_str = "dbname='{self.dbname}' user='{self.user}' host='{self.host}' password='{self.psswrd}'" .format(self=self)

        try:
            self.conn = psycopg2.connect(connection_str)
            self.conn.autocommit = True
        except:
            print "Unable to connect to the database"
        return self.conn
        
    def crsr(self):
        cur = self.cnct().cursor()
        return cur
