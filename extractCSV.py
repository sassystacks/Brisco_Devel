import datetime as dt
import csv

class ExtractCSV:

    def __init__(self,connect_instance,fname,month,year):
        self.fname = fname
        self.month = month
        self.year = year
        self.connect_instance = connect_instance
        self.cur = connect_instance.crsr()

    def WriteCSV(self):
        # date1 = dt.date(self.year,self.month,1)
        # date2 = dt.date(self.year,self.month+1,1)
        # exec_statement = """SELECT * from {self.sheet_name}"""
        self.cur.execute("""SELECT *
                            FROM barkieshauling_2016_2017
                            WHERE date_entered::date >= %s AND date_entered::date <%s;""",(dt.date(self.year,self.month,1),dt.date(self.year,self.month+1,1)))
        full_DB_list = self.cur.fetchall()
        millnum=8641
        indx_csv_DB1 = [1,6,7]
        indx_csv_DB2 = [8,2,14,15,16,4,3]

        with open(self.fname, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(csv_list)
