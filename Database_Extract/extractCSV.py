import datetime as dt
import itertools

class ExtractCSV:

    def __init__(self,connect_instance,fname,month,year):
        self.fname = fname
        self.month = month
        self.year = year
        self.connect_instance = connect_instance

        self.ListInit = []
        self.lstpopinit = ['726','720','730','740','750','760','780','785']
        self.initializeLists()

        self.full_table = 'testscale'

        self.DB_list = ['daterecieved',
                    'poploadslip',
                    'count',
                    'sampleloads' ,
                    'tm9_ticket',
                    'owner' ,
                    'disposition_fmanum' ,
                    'workingcircle' ,
                    'blocknum',
                    'loggingco' ,
                    'haulingcontractor',
                    'truckplate',
                    'trucknum' ,
                    'truckaxle' ,
                    'grossweight',
                    'tareweight',
                    'netweight',
                    ]
    def _replaceSample(self,x):
        if x == '':
            return 'N'
        elif x == 'SAMPLE':
            return 'Y'
        else:
            return x

    def query_db_date(self,q_list,table,*args):
        from psycopg2 import sql
        import tkMessageBox

        cur = self.connect_instance.crsr()

        query = sql.SQL("SELECT {0} FROM {1} WHERE daterecieved::date >= %s AND daterecieved::date < %s ").format(
            sql.SQL(', ').join([sql.Identifier(n) for n in q_list]),sql.Identifier(table))
        cur.execute(query,[dt.date(self.year,self.month,1),dt.date(self.year,self.month+1,1)])

        rows = list(cur.fetchall())

        sorted_list = map(list, itertools.izip_longest(*rows))
        dict_to_write = dict(zip(q_list,sorted_list))

        if args:
            try:

                for i,val in enumerate(dict_to_write['sampleloads']):
                    if val == 0:
                        dict_to_write['sampleloads'][i] = args[0]
                    else:
                        dict_to_write['sampleloads'][i] = args[1]
            except:
                tkMessageBox.showinfo("WHOOPS!","Something Went Wrong!")
                cur.close()
        cur.close()

        return dict_to_write

    def WriteGovCSV(self):

        millnum = 8641
        month_year = str(self.month) + str(self.year)

        indx = [1,6,7,8,2,14,15,16,4,3]
        db_query_list = [self.DB_list[x] for x in indx]

        dict_gov = self.query_db_date(db_query_list,self.full_table,'N','Y')

        gov_lst = []
        loopL = len(dict_gov[db_query_list[0]])
        for x in range(0,loopL):
            a = [millnum] + [dict_gov[key][x] for key in db_query_list[:3]] + [month_year] + [dict_gov[key][x] for key in db_query_list[3:]]
            gov_lst.append(a)
        gov_lst = sorted(gov_lst)
        self.write_to_Csv(gov_lst,0)


    def WriteHaulSummaryCSV(self):


        dict_Hauling = self.query_db_date(self.DB_list,self.full_table,None,'SAMPLE')

        Haul_list = []
        loopL = len(dict_Hauling[self.DB_list[0]])
        for x in range(0,loopL):

            lst_loadslip = [None]*8
            lst_tm9 = [None]*8
            lst_intpop = map(int,self.lstpopinit)
            i = lst_intpop.index(dict_Hauling[self.DB_list[1]][x])
            lst_loadslip[i]=dict_Hauling[self.DB_list[2]][x]
            lst_tm9[i] = dict_Hauling[self.DB_list[4]][x]
            lst_remain = [dict_Hauling[key][x] for key in self.DB_list[5:]]
            row = [dict_Hauling[self.DB_list[0]][x]] + lst_loadslip + [dict_Hauling[self.DB_list[3]][x]] + lst_tm9 + lst_remain

            Haul_list.append(row)

        print row

        self.write_to_Csv(Haul_list,1)


    def WriteVbySCSV(self):

        indx = [0,4,5,6,7,8,9,12]
        db_query_list = [self.DB_list[x] for x in indx]

        dict_for_write = self.query_db_date(db_query_list,self.full_table)

        loopL = len(dict_for_write[db_query_list[0]])
        VbyS_lst = []
        for i in range(0,loopL):
            tot_list=[None]*69
            for x in [1,41,48]:
                tot_list[x] = dict_for_write['tm9_ticket'][i]
            for x in [12,15,18]:
                tot_list[x] = dict_for_write['owner'][i]
            tot_list[0] = dict_for_write['daterecieved'][i].strftime("%d-%B")
            tot_list[2] = dict_for_write['disposition_fmanum'][i]
            tot_list[3] = dict_for_write['blocknum'][i]
            tot_list[13] = dict_for_write['loggingco'][i]
            tot_list[14] = dict_for_write['trucknum'][i]
            VbyS_lst.append(tot_list)
        print(tot_list)
        self.write_to_Csv(VbyS_lst)

    def initializeLists(self):


        GovCSVList = ['Mill Number','Population #','Disposition','Working Circle',
        'Month/Year','Cut Block','Load Number','Gross','Tare','Net','TM9 Number','Sample']


        listheader1 = ['Owner','Disposition/FMA#','Working Circle',
        'Block #','Logging Co.','Hauled By','Truck License Plate #',
        'Truck #','Truck Axle','Gross Weight','Tare Weight','Net Weight','Received # of Pieces']

        listheader2 = []

        lstpopnum = []
        lsttm9 = []
        for entr in self.lstpopinit:
            popnum = ''.join(['pop. ',entr,' Load slip #'])
            tm9 = ''.join(['pop. ',entr,' TM9 #'])
            lstpopnum.append(popnum)
            lsttm9.append(tm9)
        list_barkies_hauling = ['Date'] + lstpopnum + ['Sample Loads'] + lsttm9 + listheader1


        self.ListInit.append(GovCSVList)
        self.ListInit.append(list_barkies_hauling)

    def create_dict(self):
        pass


    def write_to_Csv(self,lst,*args):
        import csv
        with open(self.fname, "wb") as f:
            writer = csv.writer(f)
            if args:
                writer.writerow(self.ListInit[args[0]])
            writer.writerows(lst)
