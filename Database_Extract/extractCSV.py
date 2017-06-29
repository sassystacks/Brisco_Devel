import datetime as dt
import csv

class ExtractCSV:

    def __init__(self,connect_instance,fname,month,year):
        self.fname = fname
        self.month = month
        self.year = year
        self.connect_instance = connect_instance
        self.cur = connect_instance.crsr()
    def _replaceSample(self,x):
        if x == '':
            return 'N'
        elif x == 'SAMPLE':
            return 'Y'
        else:
            return x

    def WriteCSV(self):
        # date1 = dt.date(self.year,self.month,1)
        # date2 = dt.date(self.year,self.month+1,1)
        # exec_statement = """SELECT * from {self.sheet_name}"""
        self.cur.execute("""SELECT *
                            FROM barkies_db
                            WHERE daterecieved::date >= %s AND daterecieved::date <%s;""",(dt.date(self.year,self.month,1),
                            dt.date(self.year,self.month+1,1)))
        full_DB_list = self.cur.fetchall()
        millnum=8641
        month_year = str(self.month) + str(self.year)
        lst_indx1 =[1,6,7]
        lst_indx2 =[8,2,14,15,16,4,3]

        lst_gov =[]
        for row in full_DB_list:
            a = [row[i] for i in lst_indx1]
            c = [row[i] for i in lst_indx2]
            b = [millnum] + a + [month_year] + c
            sample = b[-1]
            if sample == 'SAMPLE':
                sample = 'Y'
            else:
                sample = 'N'
            b[-1] = sample
            lst_gov.append(b)



        with open(self.fname, "wb") as f:
            writer = csv.writer(f)
            writer.writerow(['Mill Number','Population #','Disposition','Working Circle',
            'Month/Year','Cut Block','Load Number','Gross','Tare','Net','TM9 Number','Sample'])
            writer.writerows(lst_gov)
